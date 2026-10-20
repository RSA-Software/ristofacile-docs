# Strumenti di UI Automation per il collaudo a video delle app MAUI su Windows (R3). Si include con . .\uia.ps1
Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, System.Drawing, System.Windows.Forms
$A = [System.Windows.Automation.AutomationElement]
$T = [System.Windows.Automation.TreeScope]

$script:esiti = @()
function Verifica([bool] $cond, [string] $nome, $dato = '') {
	$script:esiti += $cond
	Write-Host (($(if ($cond) { 'ok       ' } else { 'FALLITO  ' })) + $nome + $(if (-not $cond -and $dato) { "  dato: $dato" } else { '' }))
}
function Riepilogo { $f = @($script:esiti | Where-Object { -not $_ }).Count; Write-Host "Superati: $(@($script:esiti).Count - $f). Falliti: $f."; return $f }

function Finestra([int] $processo, [int] $secondi = 60) {
	$fine = (Get-Date).AddSeconds($secondi)
	$c = New-Object System.Windows.Automation.PropertyCondition($A::ProcessIdProperty, $processo)
	while ((Get-Date) -lt $fine) {
		$w = $A::RootElement.FindFirst($T::Children, $c)
		if ($w) { return $w }
		Start-Sleep -Milliseconds 500
	}
	return $null
}

function Tutti($radice) { return $radice.FindAll($T::Descendants, [System.Windows.Automation.Condition]::TrueCondition) }

# Il primo elemento il cui nome contiene il testo (o lo eguaglia con -Esatto), entro i secondi dati.
function Cerca($radice, [string] $testo, [int] $secondi = 15, [switch] $Esatto) {
	$fine = (Get-Date).AddSeconds($secondi)
	do {
		foreach ($e in (Tutti $radice)) {
			$n = $e.Current.Name
			if ($n -and (($Esatto -and $n -eq $testo) -or (-not $Esatto -and $n.Contains($testo)))) { return $e }
		}
		Start-Sleep -Milliseconds 500
	} while ((Get-Date) -lt $fine)
	return $null
}

function Testi($radice) { return (Tutti $radice | ForEach-Object { $_.Current.Name } | Where-Object { $_ }) -join ' | ' }

function Premi($el) {
	$p = $null
	if ($el.TryGetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern, [ref] $p)) { $p.Invoke(); return $true }
	return $false
}

function Campi($radice) {
	$c = New-Object System.Windows.Automation.PropertyCondition($A::ControlTypeProperty, [System.Windows.Automation.ControlType]::Edit)
	return @($radice.FindAll($T::Descendants, $c))
}

function Scrivi($el, [string] $testo) {
	$p = $null
	if ($el.TryGetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern, [ref] $p)) { $p.SetValue($testo); return $true }
	return $false
}

function Foto($finestra, [string] $file) {
	$r = $finestra.Current.BoundingRectangle
	if ($r.Width -le 0) { return }
	$b = New-Object System.Drawing.Bitmap([int] $r.Width, [int] $r.Height)
	$g = [System.Drawing.Graphics]::FromImage($b)
	$g.CopyFromScreen([int] $r.X, [int] $r.Y, 0, 0, $b.Size)
	$b.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)
	$g.Dispose(); $b.Dispose()
}

# Le Preferences di un'app MAUI non impacchettata: JSON { "": { chiave: valore } }.
function Preferenze([string] $file, [hashtable] $valori) {
	$j = Get-Content $file -Raw | ConvertFrom-Json
	$sezione = $j.''
	foreach ($k in $valori.Keys) {
		if ($null -eq $valori[$k]) { $sezione.PSObject.Properties.Remove($k) }
		elseif ($sezione.PSObject.Properties[$k]) { $sezione.$k = [string] $valori[$k] }
		else { $sezione | Add-Member -NotePropertyName $k -NotePropertyValue ([string] $valori[$k]) }
	}
	[IO.File]::WriteAllText($file, ($j | ConvertTo-Json -Depth 5 -Compress), (New-Object System.Text.UTF8Encoding($false)))
}

Add-Type -Name Primo -Namespace Uia -MemberDefinition '[DllImport("user32.dll")] public static extern bool SetForegroundWindow(System.IntPtr h);'
function Tasto($finestra, [string] $tasti) {
	[Uia.Primo]::SetForegroundWindow([IntPtr] $finestra.Current.NativeWindowHandle) | Out-Null
	Start-Sleep -Milliseconds 500
	[System.Windows.Forms.SendKeys]::SendWait($tasti)
}

Add-Type -Name Mouse -Namespace Uia -MemberDefinition '[DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y); [DllImport("user32.dll")] public static extern void mouse_event(int f, int x, int y, int d, int e);'
# Clic vero del mouse al centro dell'elemento (per i riquadri con TapGestureRecognizer, che UIA non invoca).
function Clicca($el) {
	$r = $el.Current.BoundingRectangle
	if ($r.Width -le 0) { return $false }
	[Uia.Mouse]::SetCursorPos([int]($r.X + $r.Width / 2), [int]($r.Y + $r.Height / 2)) | Out-Null
	Start-Sleep -Milliseconds 150
	[Uia.Mouse]::mouse_event(2, 0, 0, 0, 0); Start-Sleep -Milliseconds 60; [Uia.Mouse]::mouse_event(4, 0, 0, 0, 0)
	return $true
}

Add-Type -Name Davanti -Namespace Uia -MemberDefinition '[DllImport("user32.dll")] public static extern System.IntPtr GetForegroundWindow(); [DllImport("user32.dll")] public static extern void keybd_event(byte k, byte s, int f, int e); [DllImport("user32.dll")] public static extern bool ShowWindow(System.IntPtr h, int c);'
# Porta davvero la finestra in primo piano (Alt sblocca SetForegroundWindow); false se non ci riesce.
function Davanti($finestra) {
	$h = [IntPtr]$finestra.Current.NativeWindowHandle
	for ($i = 0; $i -lt 5; $i++) {
		[Uia.Davanti]::keybd_event(0x12, 0, 0, 0); [Uia.Davanti]::keybd_event(0x12, 0, 2, 0)
		[Uia.Davanti]::ShowWindow($h, 5) | Out-Null
		[Uia.Primo]::SetForegroundWindow($h) | Out-Null
		Start-Sleep -Milliseconds 400
		if ([Uia.Davanti]::GetForegroundWindow() -eq $h) { return $true }
	}
	return $false
}
# Clic solo con la finestra davanti.
function ClicSu($finestra, $el) {
	if (-not (Davanti $finestra)) { Write-Host 'FINESTRA NON IN PRIMO PIANO: clic annullato'; return $false }
	return (Clicca $el)
}

# --- aggiunte per il manuale ---
$global:Exe = @{
	cassa   = 'C:\RSA.NET\RistoFacile\bin\Debug\net10.0-windows10.0.19041.0\win-x64\RistoFacile.exe'
	palmare = 'C:\RSA.NET\RistoFacile\RistoApp\bin\Debug\net10.0-windows10.0.19041.0\win-x64\RistoApp.exe'
	kds     = 'C:\RSA.NET\RistoFacile\RistoKds\bin\Debug\net10.0-windows10.0.19041.0\win-x64\RistoKds.exe'
}
$global:Proc = @{ cassa = 'RistoFacile'; palmare = 'RistoApp'; kds = 'RistoKds' }
function Avvia([string] $app, [int] $attesa = 12) {
	Get-Process $global:Proc[$app] -ErrorAction SilentlyContinue | Stop-Process -Force
	Start-Sleep -Milliseconds 500
	$p = Start-Process $global:Exe[$app] -PassThru
	$w = Finestra $p.Id 90
	Start-Sleep -Seconds $attesa
	return $w
}
function Win([string] $app) {
	$p = Get-Process $global:Proc[$app] -ErrorAction SilentlyContinue | Select-Object -First 1
	if (-not $p) { return $null }
	return Finestra $p.Id 10
}
$global:Shot = 'C:\Users\filippo\AppData\Local\Temp\claude\C--RSA-CLAUDE-RistoFacile\2f92d64e-beea-4f3e-8f9f-7d91753b0dd1\scratchpad\shot'
function F($w, [string] $nome) { Davanti $w | Out-Null; Start-Sleep -Milliseconds 700; Foto $w (Join-Path $global:Shot "$nome.png"); Write-Host "foto $nome" }
Add-Type -Name Pos -Namespace Uia -MemberDefinition '[DllImport("user32.dll")] public static extern bool MoveWindow(System.IntPtr h, int x, int y, int w, int hh, bool r);'
function Misura($w, [int] $x, [int] $y, [int] $larg, [int] $alt) { [Uia.Pos]::MoveWindow([IntPtr]$w.Current.NativeWindowHandle, $x, $y, $larg, $alt, $true) | Out-Null }
# clic in coordinate relative alla finestra
function ClicXY($w, [int] $dx, [int] $dy) {
	Davanti $w | Out-Null
	$r = $w.Current.BoundingRectangle
	[Uia.Mouse]::SetCursorPos([int]($r.X + $dx), [int]($r.Y + $dy)) | Out-Null
	Start-Sleep -Milliseconds 150
	[Uia.Mouse]::mouse_event(2, 0, 0, 0, 0); Start-Sleep -Milliseconds 60; [Uia.Mouse]::mouse_event(4, 0, 0, 0, 0)
}
function Elenco($w) { Tutti $w | ForEach-Object { $c = $_.Current; if ($c.Name) { $r = $c.BoundingRectangle; '{0} [{1}] {2},{3} {4}x{5}' -f $c.Name, $c.ControlType.ProgrammaticName.Replace('ControlType.',''), [int]$r.X, [int]$r.Y, [int]$r.Width, [int]$r.Height } } }
Add-Type -Name Dwm -Namespace Uia -MemberDefinition '[StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; } [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(System.IntPtr h, int a, out RECT r, int s);'
function Foto($finestra, [string] $file) {
	$h = [IntPtr]$finestra.Current.NativeWindowHandle
	$r = New-Object Uia.Dwm+RECT
	[Uia.Dwm]::DwmGetWindowAttribute($h, 9, [ref] $r, 16) | Out-Null
	$wd = $r.R - $r.L; $ht = $r.B - $r.T
	if ($wd -le 0) { return }
	$b = New-Object System.Drawing.Bitmap($wd, $ht)
	$g = [System.Drawing.Graphics]::FromImage($b)
	$g.CopyFromScreen($r.L, $r.T, 0, 0, $b.Size)
	$b.Save($file, [System.Drawing.Imaging.ImageFormat]::Png)
	$g.Dispose(); $b.Dispose()
}
# Tocca (clic vero) il primo elemento col nome esatto (o che contiene il testo con -Parziale); -Ultimo prende l'ultimo.
function Tocca($w, [string] $testo, [switch] $Parziale, [switch] $Ultimo, [int] $secondi = 8) {
	$fine = (Get-Date).AddSeconds($secondi)
	do {
		$tutti = @(Tutti $w | Where-Object { $n = $_.Current.Name; $n -and (($Parziale -and $n.Contains($testo)) -or (-not $Parziale -and $n -eq $testo)) -and $_.Current.BoundingRectangle.Width -gt 0 })
		if ($tutti.Count) {
			$el = if ($Ultimo) { $tutti[-1] } else { $tutti[0] }
			if ($el.Current.ControlType.ProgrammaticName -eq 'ControlType.Button' -and (Premi $el)) { Start-Sleep -Milliseconds 900; return $true }
			ClicSu $w $el | Out-Null; Start-Sleep -Milliseconds 900; return $true
		}
		Start-Sleep -Milliseconds 400
	} while ((Get-Date) -lt $fine)
	Write-Host "NON TROVATO: $testo"; return $false
}
function Ini { . 'C:\Users\filippo\AppData\Local\Temp\claude\C--RSA-CLAUDE-RistoFacile\2f92d64e-beea-4f3e-8f9f-7d91753b0dd1\scratchpad\uia.ps1' }
# Sceglie una voce di una tendina (ComboBox) per nome della tendina e testo della voce.
function Scegli($w, [string] $tendina, [string] $voce) {
	$cb = @(Tutti $w | Where-Object { $_.Current.Name -eq $tendina -and $_.Current.ControlType.ProgrammaticName -eq 'ControlType.ComboBox' })[0]
	if (-not $cb) { Write-Host "tendina $tendina non trovata"; return $false }
	$p = $null
	if ($cb.TryGetCurrentPattern([System.Windows.Automation.ExpandCollapsePattern]::Pattern, [ref] $p)) { $p.Expand(); Start-Sleep -Milliseconds 800 }
	$it = @($cb.FindAll($T::Descendants, [System.Windows.Automation.Condition]::TrueCondition) | Where-Object { $_.Current.Name -like "*$voce*" })
	if (-not $it.Count) { $it = @(Tutti $w | Where-Object { $_.Current.ControlType.ProgrammaticName -eq 'ControlType.ListItem' -and $_.Current.Name -like "*$voce*" }) }
	if (-not $it.Count) { Write-Host "voce $voce non trovata; voci: " + ((@($cb.FindAll($T::Descendants, [System.Windows.Automation.Condition]::TrueCondition)) | % { $_.Current.Name }) -join ','); return $false }
	$s = $null
	if ($it[0].TryGetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern, [ref] $s)) { $s.Select() } else { Clicca $it[0] | Out-Null }
	Start-Sleep -Milliseconds 500
	if ($p) { try { $p.Collapse() } catch {} }
	return $true
}
# Sceglie una voce nella tendina numero $indice (0 = prima; -1 = ultima) fra quelle visibili.
function ScegliN($w, [int] $indice, [string] $voce) {
	$cbs = @(Tutti $w | Where-Object { $_.Current.ControlType.ProgrammaticName -eq 'ControlType.ComboBox' -and $_.Current.BoundingRectangle.Width -gt 0 })
	$cb = $cbs[$indice]
	$p = $null
	$cb.TryGetCurrentPattern([System.Windows.Automation.ExpandCollapsePattern]::Pattern, [ref] $p) | Out-Null
	$p.Expand(); Start-Sleep -Milliseconds 800
	$it = @($cb.FindAll($T::Descendants, [System.Windows.Automation.Condition]::TrueCondition) | Where-Object { $_.Current.Name -eq $voce })
	if (-not $it.Count) { Write-Host "voce $voce non trovata"; $p.Collapse(); return $false }
	$s = $null
	if ($it[0].TryGetCurrentPattern([System.Windows.Automation.SelectionItemPattern]::Pattern, [ref] $s)) { $s.Select() }
	Start-Sleep -Milliseconds 400
	try { $p.Collapse() } catch {}
	return $true
}
function CampoPh($w, [string] $ph) { return @(Campi $w | Where-Object { $_.Current.Name -eq $ph })[0] }

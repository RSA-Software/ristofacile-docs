. 'C:\Users\filippo\AppData\Local\Temp\claude\C--RSA-CLAUDE-RistoFacile\2f92d64e-beea-4f3e-8f9f-7d91753b0dd1\scratchpad\uia.ps1'
$w = Win cassa
function NuovaSezione([string] $nome, [string] $uscita) {
	Tocca $w '+ Sezione' | Out-Null; Start-Sleep 2
	Scrivi (CampoPh $w 'es. Antipasti') $nome | Out-Null
	ScegliN $w -1 $uscita | Out-Null
	Tocca $w 'Salva' -Ultimo | Out-Null; Start-Sleep 3
	Write-Host "sezione $nome"
}
function Piatto([string] $cerca, [string] $nome, [string] $centro) {
	Scrivi (CampoPh $w 'Cerca un articolo…') $cerca | Out-Null; Start-Sleep -Milliseconds 1800
	if (-not (Tocca $w $nome)) { return }
	Start-Sleep -Milliseconds 1500
	if ($centro) { Tocca $w $centro | Out-Null }
	if (-not (Tocca $w 'Aggiungi')) { Tocca $w 'Annulla' | Out-Null; Write-Host "  ?? $nome"; return }
	Start-Sleep 2
	Write-Host "  + $nome"
}
# ANTIPASTI e' gia' creata, con l'antipasto completo
Piatto 'ANTIPASTO VEG' 'ANTIPASTO VEGETARIANO' 'CUCINA 1'
Piatto 'CARPACCIO' 'CARPACCIO DI BLACK ANGUS' 'CUCINA 1'
Piatto 'ANTIPASTO CALDO' 'ANTIPASTO CALDO' 'CUCINA 1'
NuovaSezione 'PRIMI' 'Primi'
Piatto 'RISOTTO' 'RISOTTO AI PORCINI' 'CUCINA 1'
Piatto 'SPAGHETTI' 'SPAGHETTI CON BOTTARGA E8.00' 'CUCINA 1'
Piatto 'RAVIOLI AI' 'RAVIOLI AI FUNGHI PORCINI E8.00' 'CUCINA 1'
Piatto 'RAVIOLI ROSSI' 'RAVIOLI ROSSI RADICCHIO E GORGONZOLA E8' 'CUCINA 1'
NuovaSezione 'SECONDI' 'Secondi'
Piatto 'FILETTO' 'FILETTO DI SCOTTONA AL PEPE ROSA' 'CUCINA 1'
Piatto 'KEBAP DI POLLO IN' 'KEBAP DI POLLO IN CESTO PASTA' 'CUCINA 1'
Piatto 'INSALATA CAPR' 'INSALATA CAPRICCIOSA' 'CUCINA 1'
Piatto 'INSALATA SAN' 'INSALATA SAN DANIELE' 'CUCINA 1'
NuovaSezione 'PIZZE' 'Secondi'
Piatto 'PIZZ0001' 'MARGHERITA' 'PIZZERIA'
Piatto 'MARINARA' 'MARINARA' 'PIZZERIA'
Piatto 'BUFALINA' 'PIZZA BUFALINA' 'PIZZERIA'
Piatto 'CALZONE' 'PIZZA CALZONE' 'PIZZERIA'
Piatto 'SCHIACCIATA' 'PIZZA SCHIACCIATA' 'PIZZERIA'
NuovaSezione 'DOLCI' 'Dessert'
Piatto 'CANNOLO DA' 'CANNOLO DA 1,80' 'BAR'
Piatto 'PORZIONE CASSATA' 'PORZIONE CASSATA' 'BAR'
Piatto 'COPPA GELATO' 'COPPA GELATO E FRUTTA' 'BAR'
NuovaSezione 'BEVANDE' 'BIBITE'
Piatto 'ACQUA NAT. CL' 'ACQUA NAT. CL 50' 'BAR'
Piatto 'ACQUA FRIZ. CL' 'ACQUA FRIZ. CL 50' 'BAR'
Piatto 'LATTINA COCA COLA' 'LATTINA COCA COLA' 'BAR'
Piatto 'LATTINA FANTA' 'LATTINA FANTA' 'BAR'
Piatto 'MENABREA' 'BIRRA MENABREA CL 33' 'BAR'
Piatto 'RIST0049' 'VINO' 'BAR'
NuovaSezione 'CAFFETTERIA' 'Dessert'
Piatto 'CAF0001' 'CAFFE CALDO' 'BAR'
Piatto 'MAROCCHINO' "CAFFE' MAROCCHINO" 'BAR'
Piatto 'AMAR0001' 'AMARO' 'BAR'
Piatto 'LIQU0005' 'LIMONCELLO' 'BAR'
Scrivi (CampoPh $w 'Cerca un articolo…') '' | Out-Null

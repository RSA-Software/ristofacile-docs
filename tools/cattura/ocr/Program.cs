using System; using System.IO; using System.Linq; using System.Threading.Tasks;
using Windows.Graphics.Imaging; using Windows.Media.Ocr; using Windows.Storage;
// ocr <immagine>: stampa una riga per linea di testo: x y w h testo
var file = await StorageFile.GetFileFromPathAsync(Path.GetFullPath(args[0]));
using var s = await file.OpenAsync(FileAccessMode.Read);
var dec = await BitmapDecoder.CreateAsync(s);
var bmp = await dec.GetSoftwareBitmapAsync(BitmapPixelFormat.Bgra8, BitmapAlphaMode.Premultiplied);
var eng = OcrEngine.TryCreateFromLanguage(new Windows.Globalization.Language("it")) ?? OcrEngine.TryCreateFromUserProfileLanguages();
var res = await eng.RecognizeAsync(bmp);
foreach (var l in res.Lines) {
  var x0 = l.Words.Min(w => w.BoundingRect.X); var y0 = l.Words.Min(w => w.BoundingRect.Y);
  var x1 = l.Words.Max(w => w.BoundingRect.X + w.BoundingRect.Width); var y1 = l.Words.Max(w => w.BoundingRect.Y + w.BoundingRect.Height);
  Console.WriteLine($"{(int)x0} {(int)y0} {(int)(x1-x0)} {(int)(y1-y0)} {l.Text}");
}

# catatan pengembangan
---

salah satu target yang ingin dicapai dalam mengembangkan sebuah interpreter adalah **kecepatan melakukan penerjemahan dari satu simbol ke simbol yang lain**, tanpa melihat "isi" dari konten tersebut.

misalnya, untuk tag markdown `#h1`:

> interpreter yang akan melakukan penerjemahan dari Markdown ke HTML hanya melihat simbol `#`, tanpa memperthatikan isi konten setelah symbol tersebut. jadi, interpreter hanya bertugas untuk "menerjemahkan" symbol `h1` dari Markdown ke tag HTML `<h1></h1>`


# teknik pemisahan konten dengan symbol
---


untuk memisahkan antara konten dengan tag Markdown,

`# ini konten`

konten: `ini konten`

markdown tag: `#`


```
In [8]: time "".join(re.findall(u'[\A-Za-z\s]', "#anu ana ana AANASAS ZAA"))
CPU times: user 63 µs, sys: 12 µs, total: 75 µs
Wall time: 73 µs
Out[8]: 'anu ana ana AANASAS ZAA'

In [9]: time "#anu ana ana AANASAS ZAA".strip("#")
CPU times: user 14 µs, sys: 2 µs, total: 16 µs
Wall time: 24.1 µs
Out[9]: 'anu ana ana AANASAS ZAA'
```

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open(input('Indique nombre del archivo, sin la extensión\t') + ".pdf", "rb"))


print("El Pdf tiene inicialmente {} paginas.\t".format(input1.getNumPages()))
print("Indique el indice de las paginas a eliminar, separadas por un espacio en blanco.\t")
skip_pages = [int(x) for x in input().split()]

for idx, x in enumerate(input1.pages):
	if idx+1 in skip_pages:
		print("Pagina {} Omitida".format(str(idx+1)))
	else:
		output.addPage(input1.getPage(idx))
		
print("El pdf resultante tiene {} paginas".format(output.getNumPages()))
outputStream = open(input('Indique el nombre del archivo resultante:\t')+".pdf", "wb")
output.write(outputStream)

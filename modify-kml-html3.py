# coding=utf-8
import xml.etree.ElementTree as ET
import csv
from bs4 import BeautifulSoup
import sys


def writecsv():
    with open('doc.kml', 'rt', encoding='utf8') as f:
        kml_file_tree = ET.parse(f)

    with open('temp.csv', mode='w', encoding='utf8', newline='') as r:
        writer = csv.writer(r)
        writer.writerow(["Productora,C,50", "Código,C,10", "CCN51_Pr,N,10,0", "CCN51_NoPr,N,10,0", "Nacnl_Pr,N,10,0", "Nacnl_NoPr,N,10,0", "SprArbl_Pr,N,10,0", "SpAbl_NoPr,N,10,0", "ha,N,13,11", "m2,N,10,0", "Comunidad,C,50", "fotoDuena,C,254", "Fecha_leva,D", "Zona,C,50", "foto_probl,N,5,0", "Problema,N,10,0"])

        for node in kml_file_tree.iter('{http://www.opengis.net/kml/2.2}Placemark'):
            # Get name element
            name = node.find('.//{http://www.opengis.net/kml/2.2}name')
            if name is not None:
                namestr = name.text
            else:
                namestr = None

            csvlist = [namestr]

            # Get Código element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(3) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(3) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get CCN51_Pr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(4) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(4) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get CCN51_NoPr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(5) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(5) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Nacnl_Pr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(6) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(6) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Nacnl_NoPr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(7) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(7) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get SprArbl_Pr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(8) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(8) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get SpAbl_NoPr element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(9) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(9) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get ha element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(10) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(10) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get m2 element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(11) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(11) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Comunidad element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(12) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(12) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get fotoDuena element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(13) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(13) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Fecha_leva element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(14) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(14) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Zona element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(15) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(15) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get foto_prob1 element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(16) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(16) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Problema element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(17) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(17) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get Cod_correg element from within HTML
            description = node.find('.//{http://www.opengis.net/kml/2.2}description')
            if description is not None:
                desc_html = description.text
                # Use BeautifulSoup to parse the HTML in desc_html
                soup = BeautifulSoup(desc_html, 'html.parser')
                desc_html = soup.select_one("table tr:nth-of-type(18) td:nth-of-type(2)")
                # Needed as some description elements do not contain a Código element
                if desc_html is not None:
                    desc_html = soup.select_one("table tr:nth-of-type(18) td:nth-of-type(2)").get_text()
                else:
                    desc_html = None
            else:
                desc_html = None

            csvlist.append(desc_html)

            # Get coords
            coords = node.find('.//{http://www.opengis.net/kml/2.2}coordinates')
            if name is not None:
                coordsstr = coords.text
                nowhitespacecoords = coordsstr.strip()
            else:
                nowhitespacecoords = None

            csvlist.append(nowhitespacecoords)

            print(csvlist)
            writer.writerow(csvlist)


writecsv()


# Take the csv and create the KML file #

csvfile = open('temp.csv')
data = csv.reader(csvfile, delimiter=',', lineterminator="\n")
# Skip the 1st header row.
next(data)
# Open the file to be written.
f = open('modified.kml', 'w')

# Writing the kml file.
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\" xmlns:gx=\"http://www.google.com/kml/ext/2.2\" xmlns:kml=\"http://www.opengis.net/kml/2.2\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n")
f.write("xsi:schemaLocation=\"http://www.opengis.net/kml/2.2 http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd http://www.google.com/kml/ext/2.2 http://code.google.com/apis/kml/schema/kml22gx.xsd\">\n")
f.write("<Document>\n")
f.write("<name>" + 'Chacras Consolidado.kml' + "</name>\n")
f.write("    <Folder id=\"FeatureLayer0\">\n")
f.write("        <name>Chacras_cacao</name>\n")
f.write("        <Snippet maxLines=\"0\"></Snippet>\n")

# Initialise 'Placemark id' counter
x = 00000

# Loop over rows in csv file
for row in data:
    f.write("        <Placemark id=\"ID_" + str(x).zfill(5) + "\">" + "\n")
    f.write("            <name>" + str(row[0]) + "</name>\n")
    f.write("            <Snippet maxLines=\"0\"></Snippet>\n")
    f.write("            <description><![CDATA[<html xmlns:fo=\"http://www.w3.org/1999/XSL/Format\" xmlns:msxsl=\"urn:schemas-microsoft-com:xslt\">\n")
    f.write("\n")
    f.write("<head>\n")
    f.write("\n")
    f.write("<META http-equiv=\"Content-Type\" content=\"text/html\">\n")
    f.write("\n")
    f.write("<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\n")
    f.write("\n")
    f.write("</head>\n")
    f.write("\n")
    f.write("<body style=\"margin:0px 0px 0px 0px;overflow:auto;background:#F4FFDC;\">\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\" >\n")
    f.write("\n")
    f.write("<div align=\"center\">\n")
    f.write("<td><img src=\"" + str(row[11]) + "\" alt=\"Foto dueña\" alt=\"Foto dueña\" width=\"400\" height=\"400\"></td>" + "\n")
    f.write("</div>\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr>\n")
    f.write("\n")
    f.write("<td>\n")
    f.write("\n")
    f.write("<table style=\"font-family:Arial,Verdana,Times;font-size:12px;text-align:left;width:100%;border-spacing:0px; padding:3px 3px 3px 3px\">\n")
    f.write("\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\">\n")
    f.write("\n")
    f.write("<td>Comunidad</td>\n")
    f.write("<td><b>" + str(row[10]) + "</b></td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr>\n")
    f.write("\n")
    f.write("<td><b>Código de la chacra</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[1]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\">\n")
    f.write("\n")
    f.write("<td><b>CCN51 productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[2]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr>\n")
    f.write("\n")
    f.write("<td><b>CCN51 no productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[3]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\">\n")
    f.write("\n")
    f.write("<td><b>Nacional productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[4]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr>\n")
    f.write("\n")
    f.write("<td><b>Nacional no productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[5]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\">\n")
    f.write("\n")
    f.write("<td><b>Super árbol productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[6]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr>\n")
    f.write("\n")
    f.write("<td><b>Super árbol no productivo</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[7]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("<tr bgcolor=\"#C4FF33\">\n")
    f.write("\n")
    f.write("<td><b>Área (hectáreas)</b></td>\n")
    f.write("\n")
    f.write("<td>" + str(row[8]) + "</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("</table>\n")
    f.write("\n")
    f.write("</td>\n")
    f.write("\n")
    f.write("</tr>\n")
    f.write("\n")
    f.write("</table>\n")
    f.write("\n")
    f.write("</body>\n")
    f.write("\n")
    f.write("</html>]]></description>\n")
    f.write("            <styleUrl>#PolyStyle0028</styleUrl>\n")
    f.write("                <MultiGeometry>\n")
    f.write("                    <Polygon>\n")
    f.write("                        <outerBoundaryIs>\n")
    f.write("                            <LinearRing>\n")
    f.write("                                <coordinates>\n")
    f.write("                                     " + str(row[17]))
    f.write("                                </coordinates>\n")
    f.write("                            </LinearRing>\n")
    f.write("                        </outerBoundaryIs>\n")
    f.write("                    </Polygon>\n")
    f.write("                </MultiGeometry>\n")
    f.write("            </Placemark>\n")
    x += 1

f.write("</Folder>\n")
f.write("</Document>\n")
f.write("</kml>\n")
f.close()

# Write .kml file
print("File Created. ")
print("Press ENTER to exit. ")
#input()

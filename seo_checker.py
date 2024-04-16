import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from requests.exceptions import RequestException, Timeout
from SeoKeywordResearch import SeoKeywordResearch


"""
1. Title tag má vhodnú dĺžku
2. Favicon
3. Meta popis
4. Meta kľúčové slová
5. HTTPS protokol
6. Dĺžka URL adresy
7. Formát URL adresy
8. Verzie URL adresy
9. Viewport meta tag
10. Robots meta tag
11. Lang atribút
12. Hreflang atribút
13. Kanonický odkaz
14. Noindex atribút
15. Noindex header
16. Open Graph protokol
17. Schema markup
18. Robots.txt
19. Sitemap.xml
20. Jeden nadpis H1 
21. Počet nadpisov H2 
22. Hierarchia nádpisov H1-H6
23. Obrázky majú atribúty width a height
24. Alt texty
25. Prvky formulárov majú priradené štítky
26. Tlačidlá majú dostupný názov
27. Pomer textu k HTML
28. HTML podľa W3C
29. Veľkosť DOM
30. Značka iFrame
31. Inline CSS
32. Veľkosť stránky  
33. Požiadavky na zdroje
34. Vlastná chybová stránka 404
35. Veľkosť obrázkov(trva DLHO)
36. Funkčné interné odkazy (trva DLHO)
37. Výkonnosť stránky podľa Google PageSpeed Insights (trva DLHO)
38. Prepojenie s Google Analytics
39. Nechránené e-mailové adresy
40. GZIP kompresia
41. CSS mediálne dopyty
42. Minifikované CSS súbory
43. Kódovanie znakov
44. Meta refresh tag
45. ARIA atribúty
"""


class SEOChecker:
    def __init__(self):
        pass
        
    
    def check_title_tag_length(self, url):
        test_name = "Title tag"
        tip="Ideálna dĺžka pre title tag je  30 až 60 znakov. Po presiahnutí počtu znakov Google title tag začína orezávať."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                title = soup.title.string.strip() if soup.title else None

                # skontroluj ci je na stranke title a ci ma medzi 30-60 znakov
                if title and 30 <= len(title) <= 60:
                    status = "passed"
                    message = f"Title tag má vhodnú dĺžku ({len(title)} znakov)"

                else:
                    status = "failed"
                    message = f"Title tag nemá vhodnú dĺžku ({len(title)} znakov)"
                
                results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def check_favicon(self, url):
        test_name = "Favicon"
        tip="Favicon prispieva k lepšej používateľskej skúsenosti, rozpoznaniu značky a  zlepšeniu miery prekliknutia."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje <link> tag s rel="icon" alebo rel="shortcut icon"
                favicon_link_tags = soup.find_all("link", rel=["icon", "shortcut icon"])


                if favicon_link_tags:
                    status = "passed"
                    message = "Stránka používa favicon"
                else:
                    status = "failed"
                    message = "Stránka nepoužíva favicon"

                results.extend([test_name, status, message, tip])



        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results
    

    def check_meta_description_length(self, url):
        test_name = "Meta popis"
        tip="Udržte dĺžku popisu v rozmedzí 70 až 155 znakov. Získate tak najlepšie vyzerajúci popis na všetkých zariadeniach bez orezaní."
        results = []
        status = "failed"  
        
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                meta_description_tag = soup.find("meta", attrs={"name": "description"})
                if not meta_description_tag:
                    status="failed"
                    message = "Meta popis sa nenašiel"
                elif  meta_description_tag:
                    meta_description_content = meta_description_tag.get("content")
                    message = ""  
                    if (
                        meta_description_content
                        and len(meta_description_content) >= 70
                        and len(meta_description_content) <= 155
                    ):
                        status = "passed"  
                        message = f"Meta popis má vhodnú dĺžku ({len(meta_description_content)} znakov)"
                    else:
                        message = f"Meta popis nemá vhodnú dĺžku ({len(meta_description_content)} znakov)"
                
                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results

    def check_meta_keywords(self, url):
        test_name = "Meta kľúčové slová"
        tip="Meta keywords predstavuje zastaranú značku. Jej používanie môžu niektoré vyhľadávače považovať za signál spamu."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:


                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi <meta> tag s name="keywords"
                meta_keywords_tag = soup.find("meta", attrs={"name": "keywords"})

                if meta_keywords_tag:
                    status = "failed"
                    message = "Meta keywords tag je prítomný"
                else:
                    status = "passed"
                    message = "Meta keywords tag nie je prítomný"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results

    def check_https(self, url):
        test_name = "HTTPS protokol"
        tip="HTTPS šifruje všetky údaje prenášané medzi prehliadačom používateľa a webovým serverom, čo sťažuje hackerom zachytiť alebo ukradnúť citlivé informácie, ako sú heslá a čísla kreditných kariet."
        results = []

        try:
            response = requests.get(url)

            if response.url.startswith("https://"):
                status = "passed"
                message = "Stránka používa HTTPS protokol"

            else:
                status = "failed"
                message = "Stránka nepoužíva HTTPS protokol"

            results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def check_url_length(self, url):
        test_name = "Dĺžka URL adresy"
        tip="Optimalizovaná adresa URL je informatívna a má menej než 255 znakov."
        results = []

        try:
            # Skontroluj ci dlzka URL je menej ako 255 znakov
            if len(url) < 255:
                status = "passed"
                message = "URL má vhodnú dĺžku"
            else:
                status = "failed"
                message = "URL nemá vhodnú dĺžku"

            results.extend([test_name, status, message, tip])

            
        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results

    def check_url_format(self, url):
        test_name = "Formát URL adresy"
        tip="Pre lepšiu čitateľnosť sa vyhnite číslam, veľkým písmenám a nevhodným špeciálnym znakom. Na oddeľovanie slov miesto podčiarkovníkov používajte pomlčky."
        message = ""

        results = []
        try:
            # Skontroluj ci URL obsahuje len male pismena
            if not url.islower():
                status = "failed"
                message += "URL obsahuje veľké písmená <br>"

            # Skontroluj ci URL neobsahuje nevhodne specialne symboly
            special_characters = set(' "<>#%{}|\\^~[]`')
            if any(char in special_characters for char in url):
                status = "failed"
                message += "URL obsahuje nevhodné špeciálne znaky <br>"

            # Skontroluj ci URL neobsahuje podciarkovniky
            if "_" in url:
                status = "failed"
                message += "URL obsahuje podčiarkovníky <br>"

            # Skontroluj ci URL neobsahuje cisla
            if any(char.isdigit() for char in url):
                status = "failed"
                message += "URL obsahuje čísla <br>"

            if message == "":
                status = "passed"
                message = "URL má správny formát"

            results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results

    def check_url_versions(self, url):
        test_name = "Verzie URL"
        tip="Automatické presmerovanie na jednu verziu URL po zadaní názvu webu s alebo bez skratky www pred doménou je dôležité pre zachovanie dobrej používateľskej skúsenosti."
        results = []

        try:

            parsed_url = urlparse(url)
            
            # ziskame domenu (network location)
            domain = parsed_url.netloc

            if domain.startswith("www."):
                domain_without_www = domain.replace("www.", "")
            else:
                domain_without_www = domain

            # Posli GET request na URL s www
            response_www = requests.get(f"https://www.{domain_without_www}")
            redirected_url_www = response_www.url

            # Posli GET request na URL bez www
            response_without_www = requests.get(f"https://{domain_without_www}")
            redirected_url_without_www = response_without_www.url

            # Porovnaj vysledky presmerovania
            if redirected_url_www == redirected_url_without_www:
                status = "passed"
                message = "Verzie URL s www aj bez www sú presmerované na rovnakú stránku"
            else:
                status = "failed"
                message = (
                    "Verzie URL s www aj bez www nie sú presmerované na rovnakú stránku"
                )

            results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def check_viewport_meta_tag(self, url):
        test_name = "Viewport meta tag"
        tip="Nepoužívanie značky viewport môže sťažiť čítanie webových stránok a spôsobiť značné oneskorenie v mobilnom zobrazení."
        results = []
     
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje viewport meta tag
                viewport_meta_tag = soup.find("meta", attrs={"name": "viewport"})

                if viewport_meta_tag:
                    status = "passed"
                    message = "Viewport meta tag je prítomný"
                else:
                    status = "failed"
                    message = "Viewport meta tag nie je prítomný"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def check_robots_meta_tag(self, url):
        test_name = "Robots meta tag"
        tip="Značka robots umožňuje vlastníkom webu kontrolu nad tým, ako vyhľadávače spracúvajú ich obsah, čím predchádzajú duplicitnému obsahu a indexovaniu citlivých informácií."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:
                
                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje robots meta tag
                robots_meta_tag = soup.find("meta", attrs={"name": "robots"})
                if robots_meta_tag:
                    status = "passed"
                    message = "Robots meta tag je prítomný"

                else:
                    status = "failed"
                    message = "Robots meta tag nie je prítomný"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_lang_attribute(self, url):
        test_name = "Lang atribút"
        tip="Pomocou lang atribútu môžu vyhľadávače lepšie určiť, ktorému publiku sa má váš obsah zobraziť."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                html_tag = soup.find("html")
                if html_tag:
                    lang_attribute = html_tag.get("lang")
                    if lang_attribute:
                        status = "passed"
                        message = "Lang atribút je prítomný"
                    else:
                        status = "failed"
                        message = "Lang atribút nie je prítomný"

                    results.extend([test_name, status, message, tip])

                    
                else:
                    print("<html> tag nenájdený.")

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_hreflang_attribute(self, url):
        test_name = "Hreflang atribút"
        tip="Atribút hreflang pomáha vyhľadávacím nástrojom pochopiť, ktorá verzia webovej stránky sa má používateľom zobraziť na základe ich preferencií jazyka a polohy. "
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

        
                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje hreflang atribut
                hreflang_tags = soup.find_all(hreflang=True)
                if hreflang_tags:
                    status = "passed"
                    message = "Stránka používa hreflang atribút"
                else:
                    status = "failed"
                    message = "Stránka nepoužíva hreflang atribút"

                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_canonical_link(self, url):
        test_name = "Kanonický odkaz"
        tip="Kanonický odkaz, známy aj ako značka rel='canonical' umožňuje definovať primárnu verziu v skupine duplicitných alebo takmer duplicitných stránok na vašom webe. V SEO kanonické odkazy navrhujú Googlu, ktorú verziu stránky by mal indexovať."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje canonical tag
                canonical_tag = soup.find("link", rel="canonical")
                if canonical_tag:
                    status = "passed"
                    message = "Kanonický odkaz je prítomný"
                else:
                    status = "failed"
                    message = "Kanonický odkaz nie je prítomný"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_noindex_attribute(self, url):
        test_name = "Noindex atribút"
        tip="Noindex atribút zabráni indexovaniu danej webovej stránky vyhľadávačmi."
        results = []
        status = "passed"
        message = "Stránka nepoužíva noindex atribút"
        try:
            response = requests.get(url)
            if response.status_code == 200:


                soup = BeautifulSoup(response.content, "html.parser")

                # Skontroluj ci existuje noindex meta tag
                meta_tags = soup.find_all("meta", attrs={"name": "robots"})
                for tag in meta_tags:
                    content = tag.get("content", "").lower()
                    if "noindex" in content.split(","):
                        status = "failed"
                        message = "Stránka používa noindex atribút"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_noindex_header(self, url):
        test_name = "Noindex header"
        tip="Noindex header zabráni indexovaniu danej webovej stránky vyhľadávačmi."
        results = []
        try:
            # Posli HEAD request na ziskanie headerov
            response = requests.head(url)
            if response.status_code == 200:

                # Skontroluj ci je pritomny 'noindex' header
                if "noindex" in response.headers.get("X-Robots-Tag", "").lower():
                    status = "failed"
                    message = "Stránka používa noindex header"
                else:
                    status = "passed"
                    message = "Stránka nepoužíva noindex header"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_open_graph(self, url):
        test_name = "Open Graph protokol"
        tip="Protokol Open Graph umožňuje kontrolovať, aký obrázok, názov a popis sa zobrazí pri zdieľaní odkazov na sociálnych sieťach."
        found_properties = set()
        expected_properties = {
            "og:title",
            "og:type",
            "og:image",
            "og:url",
            "og:description",
            "og:site_name",
        }
        results = []

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                meta_tags = soup.find_all(
                    "meta",
                    attrs={
                        "property": [
                            "og:title",
                            "og:type",
                            "og:image",
                            "og:url",
                            "og:description",
                            "og:site_name",
                        ]
                    },
                )

                for tag in meta_tags:
                    property_name = tag.get("property")
                    if property_name:
                        found_properties.add(property_name)

                # Najdi chybajuce properties
                missing_properties = expected_properties - found_properties

                if not missing_properties:
                    status = "passed"
                    message = "Stránka používa Open Graph protokol."
                else:
                    status = "failed"
                    message = f"Chýbajúce značky: {', '.join(missing_properties)}"

                results.extend([test_name, status, message, tip])

            else:
                print(f"Failed to access webpage. Status code: {response.status_code}")
        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_schema_markup(self, url):
        test_name = "Schema Markup"
        tip="Schema Markup je kód, ktorý pomáha vyhľadávacím nástrojom porozumieť informáciám na stránke. Google ho môže použiť na zobrazenie multimediálnych výsledkov (známych aj ako rich snippets), ktoré môžu stránke zabezpečiť viac kliknutí."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                html_content = response.text

                # Skontroluj ci su klucove slova pritomne
                schema_keywords = [
                    "schema.org",
                    "StructuredData",
                    "itemprop",
                    "itemscope",
                    "itemtype",
                ]
                schema_markup_used = any(
                    keyword.lower() in html_content.lower() for keyword in schema_keywords
                )

                if schema_markup_used:
                    status = "passed"
                    message = "Stránka používa Schema Markup"
                else:
                    status = "failed"
                    message = "Stránka nepoužíva Schema Markup"

                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results

    def check_robots_txt(self, url):
        test_name = "Robots.txt"
        tip="Súbor robots.txt je súbor pokynov, pomocou ktorých webové stránky informujú vyhľadávače, ktoré stránky by sa mali a nemali prehľadávať."
        results = []
        try:
            response = requests.get(url + "/robots.txt")
            if response.status_code == 200:
                status = "passed"
                message = "Stránka obsahuje súbor robots.txt"

            else:
                status = "failed"
                message = "Stránka neobsahuje súbor robots.txt"

            results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_sitemap_xml(self, url):
        test_name = "Sitemap.xml"
        tip="Súbor sitemap.xml je súbor, v ktorom poskytujete informácie o stránkach, videách a iných súboroch na vašej  stránke a o vzťahoch medzi nimi. Vyhľadávacie nástroje ako Google čítajú tento súbor, aby mohli efektívnejšie prehľadávať vaše stránky."
        results = []
        try:
            response = requests.get(url + "/sitemap.xml")
            if response.status_code == 200:
                status = "passed"
                message = "Stránka obsahuje súbor sitemap.xml"

            else:
                status = "failed"
                message = "Stránka neobsahuje súbor sitemap.xml"

            results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_h1_presence(self, url):
        test_name = "Jeden nadpis H1"
        tip="Pre jasnú a zmysluplnú štruktúru sa odporúča mať práve jeden nadpis H1 na stránku."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                h1_tags = soup.find_all("h1")

                if len(h1_tags) == 1:
                    status = "passed"
                    message = "Na stránke je jeden H1 nadpis"
                elif len(h1_tags) > 1:
                    status = "failed"
                    message = f"Na stránke sú {len(h1_tags)} H1 nadpisy"
                elif not h1_tags:
                    status = "failed"
                    message = "Na stránke sa nenašiel H1 nadpis"

                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_h2_tags(self, url):
        test_name = "Počet nadpisov H2"
        tip="Tagy <h2> označujú hlavné časti obsahu a na stránke sa odporúča mať aspoň 2 a viac takýchto nadpisov. "
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                h2_tags = soup.find_all("h2")

                if len(h2_tags) >= 2:
                    status = "passed"
                    message = f"Na stránke sú aspoň 2 nadpisy H2 ({len(h2_tags)})"

                else:
                    status = "failed"
                    message = f"Na stránke je málo H2 nadpisov ({len(h2_tags)})"

                results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_heading_tag_hierarchy(self, url):
        test_name = "Hierarchia nadpisov H1-H6"
        tip = "Nadpisy by sa mali používať v poradí zhora nadol, t. j. po značke <h1> by mala nasledovať značka <h2>, nie značka <h3>."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                html_content = response.content

                soup = BeautifulSoup(html_content, "html.parser")

                
                heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
                last_heading_tag_index = -1
                for heading_tag in heading_tags:
                    current_heading_tags = soup.find_all(heading_tag)
                    if current_heading_tags:
                        current_heading_tag_index = heading_tags.index(heading_tag)
                        if current_heading_tag_index < last_heading_tag_index:
                            status = "failed"
                            message = f"Nadpisy nie sú správne hierarchicky usporiadané. {heading_tag} je pred {heading_tags[last_heading_tag_index]}."
                            break
                        last_heading_tag_index = current_heading_tag_index
                else:
                    status = "passed"
                    message = "Nadpisy sú správne hierarchicky usporiadané"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error", f"Chyba: {str(e)}"])

        return results

            
    def check_alt_attributes(self, url):
        test_name = "Alt texty"
        tip = "Je dôležité pridať popisný alternatívny text obsahujúci kľúčové slová, aby čítačky obrazovky mohli stránku interpretovať pre zrakovo postihnutých"
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")
                images = soup.find_all("img")
                images_with_missing_alt = []

                for img in images:
                    alt = img.get("alt")
                    if alt is None or alt.strip() == "":
                        images_with_missing_alt.append(img)

                if images_with_missing_alt:
                    status = "failed"
                    message = f"{len(images_with_missing_alt)} obrázkom chýbajú alt tagy:"+"<br>"
                    
                    
                    
                    images_with_missing_alt_string=""
                    for img in images_with_missing_alt:
                        
                        img_str = str(img)
                        img_str = img_str.replace("<", "&lt;").replace(">", "&gt;")
                        img_str += "<br>"  


                        images_with_missing_alt_string += img_str 
                        
                        

                    message += images_with_missing_alt_string
                    
                    
                else:
                    status = "passed"
                    message = "Ku všetkým obrázkom sú priradené alt tagy"

                results.extend([test_name, status, message, tip])

        except Exception as e:
            results.extend([test_name, "error", str(e)])
            print(e)

        return results


    
    def check_url(self, url):  
            try:
                response = requests.head(url, allow_redirects=True, timeout=10)
                final_url = response.url  
                status_code = response.status_code
                if status_code == 404:
                    return "404 Not Found"  
                elif final_url != url:  
                    return None 
                elif status_code == 403:
                    return "403 Forbidden"
                elif status_code == 408:
                    return "408 Request Timeout"
                elif status_code == 999:
                    return None 
                elif status_code >= 400:
                    return "Client Error"            
                else:
                    return None  
            except (RequestException, Timeout) as e:
                return "Request Error"
            


    def check_broken_links(self, url):
        test_name = "Funkčné interné odkazy"
        tip = "Chybové stavové kódy (403, 404, 408 a pod.) vyhľadávače môžu interpretovať ako znak nedostatočnej údržby alebo zanedbania."
        status = "passed"
        results = []
        checked_links = 0
        broken_links = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                
                body_links = [link for link in soup.find_all("a") if link.find_parent("head") is None]# Specialne linky v casti head nekontrolujeme
            


                for link in body_links:
                    if checked_links >= 20:  # Limit, lebo trva dlho
                        break
                    href = link.get("href")
                    if href and not href.startswith(("mailto:", "tel:")):  # Vynechaj mailto: a tel: links
                        full_url = urljoin(url, href)
                        checked_links += 1
                        if href != "#":
                            url_check_status_code = self.check_url(full_url)  
                            if url_check_status_code:
                                status = "failed"
                                broken_links.append(full_url)

                broken_links_str = ""

                if broken_links:
                    broken_links_str = "Nefunkčné odkazy: "
                    broken_links_str += ", ".join(broken_links)
                    broken_links_str += "<br>"

                message = f"Odkazy skontrolované <br>{broken_links_str}"
                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)

        return results


    def check_inline_css(self, url):
        test_name = "Inline CSS"
        tip="Inline štýlovanie spôsobuje pomalšie načítanie stránok."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi elementy s inline stylovanim
                elements_with_inline_style = [tag for tag in soup.find_all(lambda tag: tag.get("style")) if not any(tag.find_parents(lambda parent: parent.get("style")))]


                if elements_with_inline_style:

                    status = "failed"
                    message = f"Stránka používa inline štýlovanie v {len(elements_with_inline_style)} elementoch"

                else:
                    status = "passed"
                    message = "Stránka nepoužíva inline štýlovanie"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_iframes(self, url):
        test_name = "Značka iFrame"
        tip="Prvky iFrame môžu negatívne ovplyvniť čas načítania stránky a kompatibilitu mobilných zariadení."
        results = []
        try:

            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                iframes = soup.find_all("iframe")

                if iframes:
                    status = "failed"
                    message = "Stránka používa prvky iFrame"
                else:
                    status = "passed"
                    message = "Stránka nepoužíva prvky iFrame"

                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_page_size(self, url):
        test_name = "Veľkosť stránky"
        tip="Udržiavanie veľkosti stránky pod 2 MB je dobrým krokom pre optimalizáciu výkonu a používateľského dojmu."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Ziskaj page content
                page_content = response.text

                # Zisti page size
                page_size = len(page_content)  # v Bytoch

                if page_size < 2000000:
                    status = "passed"
                    message = f"Veľkosť stránky je menej ako 2 MB ({page_size} B)"
                else:
                    status = "failed"
                    message = "Veľkosť stránky je viac ako 2 MB"

                results.extend([test_name, status, message, tip])


           
        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_image_size(self, url):
        test_name = "Veľkosť obrázkov"
        tip="Obrázky by nemali by byť príliš veľké, pretože to môže predĺžiť čas načítania stránky. V ideálnom prípade by mali mať veľkosť do 100 kB. Kompresia je vhodným spôsobom, ako zmenšiť veľkosť obrázkov bez straty kvality."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                page_content = response.text

                soup = BeautifulSoup(page_content, "html.parser")

                # Najdi image tags
                image_tags = soup.find_all("img")

                # Skontroluj velkost obrazkov
                oversized_images = []
                for img_tag in image_tags:
                    img_url = img_tag.get("src")
                    if img_url and img_url.startswith("http"):
                        img_response = requests.get(img_url, stream=True)
                        img_size_kb = round(
                            int(img_response.headers.get("content-length", 0)) / 1024
                        )

                        if img_size_kb > 100:
                            oversized_images.append(img_url)
                           

                if (oversized_images):
                    oversized_images_str=", ".join(oversized_images)
                    oversized_images_str=oversized_images_str+"<br>"
                    
                    status = "failed"
                    message = f"Niektoré obrázky sú príliš veľké:<br>"
                    message += oversized_images_str


                else:
                    status = "passed"
                    message = "Všetky obrázky sú menšie ako 100 kB"

                results.extend([test_name, status, message, tip])

                
            

                
        except Exception as e:
            results.extend([test_name, "error"])
            print(e)
            
        return results


    def check_page_objects(self,url):
        test_name = "Objekty stránky"
        tip="Viac ako 20 požiadaviek na zdroje (ako sú obrázky, CSS, JavaScript atď.) môže viesť k pomalému načítaniu stránky."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")

                # Najdi image tags
                images = soup.find_all("img")

                # Najdi link tags s rel="stylesheet"
                stylesheets = soup.find_all("link", rel="stylesheet")

                # Najdi script tags
                scripts = soup.find_all("script", src=True)

                # Zisti pocet HTTP requestov pre kazdy zdroj
                image_count = len(images)
                stylesheet_count = len(stylesheets)
                javascript_count = len(scripts)

                total_requests = image_count + stylesheet_count + javascript_count

                if total_requests > 20:
                    status = "failed"
                    message = "Stránka posiela viac ako 20 požiadaviek, čo môže spôsobiť pomalé načítanie <br>"
                    message += f"HTTP požiadavky: {total_requests}<br>Obrázky: {image_count}<br>Stylesheet: {stylesheet_count}<br>Javascript: {javascript_count}"
                else:
                    status = "passed"
                    message = "Stránka neposiela viac ako 20 požiadaviek"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])
            print(e)
            
        return results

    
    def check_text_to_html_ratio(self, url):
        test_name = "Pomer textu k HTML"
        tip="Stránky s vysokým pomerom textu k HTML naznačujú, že stránka obsahuje podstatný obsah, ktorý je relevantný pre vyhľadávací dopyt používateľa. Ideálny pomer textu k HTML je niekde v rozmedzí 25-70%."
        results = []
        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi <body> tag
                body = soup.find("body")

                # Extrahuj text z body
                if body:
                    text = body.get_text(separator=" ")
                else:
                    text = ""

                # Zisti pocet znakov v texte z body
                text_size = len(text)

                # Zisti celkovy pocet znakov HTML dokumentu
                html_size = len(response.text)

                # Zisti pomer textu k HTML
                text_to_html_ratio = round((text_size / html_size) * 100)

                if text_to_html_ratio >= 25 and text_to_html_ratio <= 70:
                    status = "passed"
                    message = "Stránka má vhodný pomer textu k HTML"
                else:
                    status = "failed"
                    message = f"Stránka nemá vhodný pomer textu k HTML ({text_to_html_ratio}%)"

                results.extend([test_name, status, message, tip])

        except Exception as e:
            results.extend([test_name, "error"])
            print(e)
            
        return results
    
    def check_form_field_labels(self, url):
        test_name = "Prvky formulárov majú priradené štítky"
        tip="Štítky zabezpečujú, že asistenčné technológie, ako napríklad čítačky obrazovky, správne identifikujú prvky formulárov."
        results = []

        try:

            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # najdi form prvky
                form_fields = soup.find_all(["input", "textarea", "select"])

                # zisti ci maju labels
                fields_without_labels = []
                for field in form_fields:

                    if field.get("id"):
                        label = soup.find("label", {"for": field["id"]})
                        if not label:
                            fields_without_labels.append(field)

                if fields_without_labels:
                    status = "failed"
                    message = "Prvky bez štítkov:"+"<br>"
                    
                    for field in fields_without_labels:
                        field_str = str(field)
                        field_str = field_str.replace("<", "&lt;").replace(">", "&gt;")
                        field_str += "<br>"  
                        message += field_str
                else:
                    status = "passed"
                    message = "Všetky prvky formulárov majú priradený štítok"

                results.extend([test_name, status, message, tip])

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    
    def check_button_accessibility(self, url):
        test_name = "Tlačidlá majú dostupný názov"
        tip="Keď tlačidlo nemá dostupný názov, ľudia, ktorí používajú pomocné technológie, nemajú ako rozpoznať jeho účel."
        unaccessible_buttons = []
        results = []

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi buttons
                buttons = soup.find_all("button")

                for button in buttons:
                    # Zisti ci ma button dostupny nazov
                    if (
                        "title" not in button.attrs
                        and "aria-label" not in button.attrs
                        and "aria-labelledby" not in button.attrs
                        and not button.text.strip()
                    ):
                        unaccessible_buttons.append(button)

                if len(unaccessible_buttons) > 0:
                    status = "failed"
                    message = "Našlo sa tlačidlo s nedostupným názvom:"+"<br>"
                    for button in unaccessible_buttons:
                        button_str = str(button)
                        button_str=button_str.replace("<", "&lt;").replace(">", "&gt;")
                        message += f"{button_str}<br>"
                else:
                    status = "passed"
                    message = "Všetky tlačidlá majú dostupný názov"

                results.extend([test_name, status, message, tip])


                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    
    def check_image_attributes(self, url):
        test_name = "Obrázky majú atribúty width a height"
        tip="Obrázky, ktoré nemajú atribúty width a height, môžu spôsobiť zmeny rozloženia pri načítavaní stránky"
        message = ""
        results = []

        try:

            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                images = soup.find_all("img")

                if len(images) == 0:
                    status = "passed"
                    message = "Všetky obrázky majú atribúty width a height"

                for image in images:
                    # zisti ci obrazok ma width a height atributy
                    if "width" not in image.attrs or "height" not in image.attrs:
                        status = "failed"
                        message += f"{image}<br>"
                    else:
                        status = "passed"
                        message = "Všetky obrázky majú atribúty width a height"

                results.extend([test_name, status, message, tip])



        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results


    def check_custom_404_page(self, url):
        test_name = "Vlastná chybová stránka 404 "
        tip="Používanie vlastnej chybovej stránky 404 môže prispieť k lepšej používateľskej skúsenosti a zníženej miere odchodov."
        results = []

        try:
            modified_url = url + "/nonexistent-page"

            response = requests.get(modified_url)
        

            if response.status_code == 200 or response.status_code == 404:

                soup = BeautifulSoup(response.content, "html.parser")

                title_element = soup.find("title")

                if (
                    title_element is not None
                    and title_element.text.strip() == "404 Not Found"
                ):
                    status = "failed"
                    message = "Web nemá vlastnú chybovú stránku 404"

                else:
                    status = "passed"
                    message = "Web má vlastnú chybovú stránku 404"

                results.extend([test_name, status, message, tip])


                

        except Exception as e:
            results.extend([test_name, "error"])
            print(e)
        return results

    def check_w3c_validity(self, url):
        test_name = "HTML podľa W3C"
        tip="Webové štandardy sú pravidlá určené pre tvorbu web stránok, navrhované konzorciom W3C. Hlavnou úlohou konzorcia W3C je zjednocovať a modernizovať technológie používané na internete."
        results = []
        try:
            #  API endpoint URL
            api_url = "https://validator.w3.org/nu/"
            # parametre dopytu
            query_params = {
                "doc": url,
                "out": "json",
            }

            # Posli GET request pre W3C Validator API
            response = requests.get(api_url, params=query_params)

            if response.status_code == 200:

                json_data = response.json()

                warning_count = 0
                error_count = 0

                message = ""

                for text in json_data["messages"]:
                    if text.get("type") == "error":
                        status = "failed"
                        error_count += 1

                    elif text.get("subType") == "warning":
                        status = "failed"
                        warning_count += 1

                if error_count == 0 and warning_count == 0:
                    status = "passed"
                    message = "HTML je v súlade s W3C štandardami."
                else:
                    status = "failed"
                    message = f"HTML nie je v súlade s W3C štandardami. Zistilo sa {error_count} chýb a {warning_count} varovaní"

                results.extend([test_name, status, message, tip])

                

            else:
                return "Failed to fetch W3C Validator API."
        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def check_dom_elements(self, url):
        test_name = "Veľkosť DOM"
        tip="Veľký DOM môže spomaliť výkon vašej stránky. Neodporúča sa mať DOM s viac ako 1 500 uzlami."
        results = []

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi vsetky DOM elementy
                dom_elements = soup.find_all()

                total_dom_elements = len(dom_elements)

                if total_dom_elements > 1500:
                    status = "failed"
                    message = "DOM má viac ako 1500 uzlov"
                else:
                    status = "passed"
                    message = "DOM má vhodnú veľkosť"

                results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)

        return results

    def check_ga_tag(self, url):
        test_name = "Prepojenie s Google Analytics"
        tip="Google Analytics je platforma, ktorá zhromažďuje údaje z vašich webov a aplikácií s cieľom vytvárať reporty so štatistikami o vašej firme."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi vsetky script tagy
                script_tags = soup.find_all("script")

                # Regex na najenie google analytics tagu
                ga_pattern = re.compile(
                    r"(?:www\.)?googletagmanager\.com(?:/gtm\.js)?|analytics\.google\.com(?:/analytics\.js)?"
                )

                status = "failed"
                message = "Web nie je prepojený s Google Analytics"

                for script in script_tags:
                    if ga_pattern.search(str(script)):
                        status = "passed"
                        message = "Web je prepojený s Google Analytics"

                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, status, message, tip])
            print(e)

        return results

    def check_plaintext_emails(self, url):
        test_name = "Nechránené e-mailové adresy"
        tip="Odporúčame e-mailové adresy zneviditeľniť pre e-mailových pavúkov, ktorí adresy získavajú extrakciou z textu a následne rozosielajú spam. "
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Extrahuj text z HTML
                text_content = soup.get_text()

                # Regex na najdenie mailu
                email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

                emails_found = re.findall(email_pattern, text_content)

                if emails_found:
                    status = "failed"
                    message = (
                        "Text obsahuje e-mailové adresy viditeľné pre e-mailových pavúkov: "
                    )
                    for email in emails_found:
                        message+=f"{email}<br>"
                else:
                    status = "passed"
                    message = (
                        "Text neobsahuje e-mailové adresy viditeľné pre e-mailových pavúkov"
                    )

               
                results.extend([test_name, status, message, tip])

                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results

    def check_gzip_enabled(self, url):
        test_name = "GZIP kompresia"
        tip="GZIP je forma kompresie údajov. HTTP protokol umožňuje odosielanie údajov vo formáte gzip, čo znamená, že náklady na obsluhu stránky sú nižšie, pretože sú sťahované menšie súbory."
        results = []

        try:
            response = requests.head(url)  # Ziskanie hlaviciek
            if response.status_code == 200:

                if "Content-Encoding" in response.headers:
                    content_encoding = response.headers["Content-Encoding"]
                    if "gzip" in content_encoding:
                        status = "passed"
                        message = "GZIP kompresia je povolená"
                    else:
                        status = "failed"
                        message = "GZIP kompresia nie je povolená"
                else:
                    status = "failed"
                    message = "GZIP kompresia nie je povolená"

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)

        return results
        


    def check_media_queries(self, url):
        test_name = "CSS mediálne dopyty"
        tip="Stránka využíva CSS mediálne dopyty (media queries), ktoré sú nevyhnutné pre responzívny dizajn."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Ziskaj zakladnu URL stranky
                base_url = response.url

                # Najdi vsetky linky s rel="stylesheet"
                css_links = [
                    link["href"]
                    for link in soup.find_all("link", rel="stylesheet")
                    if "href" in link.attrs
                ]

                for css_link in css_links:
                    # vytvorenie absolutnej adresy URL pre subor
                    absolute_css_url = urljoin(base_url, css_link)

                    try:
                        # Ziskanie CSS obsahu
                        css_response = requests.get(absolute_css_url)
                        if css_response.status_code == 200:
                            css_content = css_response.text

                            # Zistime ci obsah ma media queries
                            if "@media" in css_content:
                                status = "passed"
                                message = "Stránka využíva CSS mediálne dopyty"
                                break  # Ak sa najde, prerusime slucku

                    except Exception as e:
                        print(
                            f"Pri načítavaní CSS z adresy sa vyskytla chyba {absolute_css_url}: {e}"
                        )
                        continue  # Pokracuj s dalsou CSS URL

                else:
                    status = "failed"
                    message = "Stránka nevyužíva CSS mediálne dopyty"

                
                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
        
        return results


    def is_minified_css(self, css_url):
        if ".min.css" in css_url:
            return True
        else:
            return False 
        
    

    def check_minified_css(self, url):
        test_name = "Minifikované CSS súbory"
        tip="Minifikácia je proces na zmenšenie veľkosti súborov tým, že sa odstránia zbytočné znaky, medzery, odsadenia a komentáre. Cieľom je zlepšiť rýchlosť načítania webovej stránky"
        results = []
        non_minified_css = []

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                base_url = response.url

                # Najdi tagy s rel="stylesheet"
                css_links = [
                    link["href"]
                    for link in soup.find_all("link", rel="stylesheet")
                    if "href" in link.attrs
                ]

                for css_link in css_links:
                    # Absolutna URL pre CSS file
                    absolute_css_url = urljoin(base_url, css_link)

                    try:

                        css_response = requests.get(absolute_css_url)
                        if css_response.status_code == 200:

                            # Skontroluj ci je subor minifikovany
                            is_minified = self.is_minified_css(absolute_css_url)
                            if not is_minified:
                                non_minified_css.append(absolute_css_url)

                    except Exception as e:
                        results.extend([test_name, "error"])

                        print(e)

                # Ak sa najdu non-minified CSS files
                if non_minified_css:
                    non_minified_message = (
                        "Našli sa neminifikované CSS súbory:<br>"
                        + "<br>".join(non_minified_css)
                    )
                    results.extend([test_name, "failed", non_minified_message, tip])
                elif not css_links:
                    results.extend([test_name, "failed", "Nenašli sa žiadne CSS súbory", tip])
                else:
                    results.extend([test_name, "passed", "CSS súbory sú minifikované", tip])
    
                

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)

        return results  

    

    def check_character_encoding_declaration(self, url):
        test_name = "Kódovanie znakov"
        tip="Deklarácia kódovania znakov zabezpečuje, že sa text zobrazuje presne."
        results = []

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # Najdi meta tag s charset deklaraciou
                charset_meta_tag = soup.find("meta", charset=True)
                if charset_meta_tag:
                    status = "passed"
                    message = "Kódovanie znakov je deklarované"
                else:
                    status = "failed"
                    message = "Kódovanie znakov nie je deklarované"
            else:
                status = "failed"
                message = f"Chyba pri získavaní stránky: {response.status_code}"

            results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])
            print(e)
            
        return results    


    def check_meta_refresh_tag(self, url):
        test_name = "Meta refresh tag"
        tip="Meta refresh tag automaticky obnovuje stránku po určitom čase a môže dezorientovať používateľov, najmä tých, ktorí sa spoliehajú na čítačky obrazovky."
        results = []

        try:
            response = requests.get(url)
            if response.status_code == 200:

                soup = BeautifulSoup(response.content, "html.parser")

                meta_refresh_tag = soup.find("meta", attrs={"http-equiv": "refresh"})

                if meta_refresh_tag:
                    status = "failed"
                    message = "Stránka používa meta resfresh tag"
                else:
                    status = "passed"
                    message = "Stránka nepoužíva meta resfresh tag"

                results.extend([test_name, status, message, tip])

            

        except Exception as e:
            results.extend([test_name, "error"])

            print(e)
            
        return results



    def check_aria_attributes(self, url):
        test_name = "ARIA atribúty"
        tip="Zahrnutie ARIA atribútov zlepšuje prístupnosť a zabezpečuje dodržiavanie štandardov."
        results = []

        try:
            response = requests.get(url)

            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                # Najdi elementy s ARIA atributmi
                elements_with_aria = soup.find_all(lambda tag: any(tag.has_attr(attr) for attr in ['role', 'aria-labelledby', 'aria-label', 'aria-describedby']))

                if elements_with_aria:
                    status = "passed"
                    message = "Stránka používa ARIA atribúty."
                else:
                    status = "failed"
                    message = "Stránka nepoužíva ARIA atribúty."

                results.extend([test_name, status, message, tip])


        except Exception as e:
            results.extend([test_name, "error"])

            print(e)


        return results




    API_KEY = "AIzaSyB-cskFBtzSYgjjii5qJ-kVqvtUY6kRr-4"
    def get_page_speed_data(self, url):
        test_name = "Výkonnosť stránky podľa Google PageSpeed Insights"
        tip = "Keď sa webová stránka načíta rýchlo, poskytuje lepšiu používateľskú skúsenosť, čo vyhľadávače vysoko oceňujú. Skóre výkonnosti stránky Google počíta podľa 6 rôznych metrík. Medzi najdôležitejšie patria Total Blockig Time, Largest Contentful Paint a Cumulative Layout Shift. Skóre od 0-49 predstavuje slabé skôre, 50-89 priemerné a 90-100 dobré."
        results = []

        try:
            endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={self.API_KEY}"
            response = requests.get(endpoint)

            data = response.json()
            basic_info = {}
            basic_info["score"] = data["lighthouseResult"]["categories"]["performance"]["score"]
            page_speed_score = int(basic_info.get("score") * 100)

            if page_speed_score < 49:
                status = "failed"
                message = f"Výkonnosť stránky podľa Google Page Speed Insights je slabá ({page_speed_score})"
            elif page_speed_score <= 89:
                status = "passed"
                message = f"Výkonnosť stránky podľa Google Page Speed Insights je priemerná ({page_speed_score})"
            else:
                status = "passed"
                message = f"Výkonnosť stránky podľa Google Page Speed Insights je dobrá ({page_speed_score})"

            results.extend([test_name, status, message, tip])

        
        except Exception as e:
            results.extend([test_name, "error", f"Chyba: {str(e)}"])

        return results
    

    def get_keyword_suggestions(self, user_keywords):

        user_keywords = user_keywords.strip()

        keyword_research = SeoKeywordResearch(

            query=user_keywords,
            api_key='4fc2ae3b7f73ec88ce154789578b08bcc9f72de1098683bd7a189337f1aec873',
            lang='sk',
            country='sk',
            domain='google.com'
        )

        auto_complete_results = keyword_research.get_auto_complete()
        related_searches_results = keyword_research.get_related_searches()
        related_questions_results = keyword_research.get_related_questions()

        data = {
            'auto_complete': auto_complete_results,
            'related_searches': related_searches_results,
            'related_questions': related_questions_results
        }

        return(data)



            
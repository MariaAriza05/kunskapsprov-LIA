Testautomationslösning i Python med Pytest

Detta projekt är en enkel testautomationslösning byggd med Python och Pytest.
Syftet är att visa grundläggande förståelse för testautomatisering, filtester, API-tester samt CI/CD med GitHub Actions.

Projektet innehåller tre olika typer av tester:

Math-test – testar en enkel matematisk funktion

File-test – testar filhantering och validering av filinnehåll

API-test – testar ett externt API (Petstore) och validerar JSON-respons

Projektet är kopplat till GitHub Actions, vilket innebär att testerna körs automatiskt vid varje push till main-branchen som en del av ett CI/CD-flöde.

Tester i projektet

Math-test

Ett enkelt test som verifierar en matematisk funktion.
Visar att Pytest är korrekt uppsatt och fungerar.

File-test

Testar att en fil kan läsas och att innehållet matchar förväntat värde.
Demonstrerar filhantering och validering av data.

API-test

Använder Petstore Swagger API för att testa en GET-endpoint.

Testet kontrollerar att:

API:et svarar med statuskod 200

svaret är JSON

JSON är en lista

listan inte är tom

Detta är ett mer avancerat API-test än grundexemplet och visar förståelse för API-testning i Pytest.

CI/CD – GitHub Actions

Projektet använder en workflow-fil (python-app.yml) som:

installerar Python och beroenden

kör Pytest automatiskt vid varje push

visar resultat direkt i GitHub Actions

Alla tre tester (math, file, API) körs i pipelinen och passerar.
Detta uppfyller kravet att minst ett test ska köras i CI/CD.
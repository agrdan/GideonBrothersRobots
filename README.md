# GideonBrothersRobots

Zadatak za selekcijski proces u Gideon Brothers-u.
Zadacai koji nisu riješeni: OpenAPI - tražio sam riješenje, ali nisam uspio naci neko gdje se autogenerira swagger.json (svako riješenje ispada da treba rucno 
pisati .json, a siguran sam da postoji intuitivnije riješenje) prema endpointima (obicno koristim FastAPI u slucaju ako mi je potrebna dokumentacija)

u zamjenu za dokumentaciju šaljem postman json sa enpointima koje sam koristio.

Drugi dio koji nije riješen je vezan za Docker, na pola je završena priprema image-a, aj jednostavno nisam stigao do kraja.
Aplikacija se vrti na mojem VPSu pa se može direktno koristiti postman import, samo je potrebna "registracija" korisnika

u folderu (postman) 
GideonBrothers->auth->registration: upisati username i password, te je tako izvršena registracija
napraviti login s registriranim podacima iznad da se dobi token, te taj token kopirati u svaki endpoint u header pod property: Auth-Token


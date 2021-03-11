# GideonBrothersRobots

Zadatak za selekcijski proces u Gideon Brothers-u.
Zadacai koji nisu riješeni: OpenAPI - tražio sam riješenje, ali nisam uspio naci neko gdje se autogenerira swagger.json (svako riješenje ispada da treba rucno 
pisati .json, a siguran sam da postoji intuitivnije riješenje) prema endpointima (obicno koristim FastAPI u slucaju ako mi je potrebna dokumentacija)

UPDATE (napravljen iza roka predaje pa se moze i nemora uzeti u selekcijski proces)
"""
image se nalazi na docker hub-u (name - agrdan/gbrobots_image:1)
- nemam puno iskustva s dockerom, buildao sam svoj image iz interaktivnog moda
projekt je na image-u checkoutan na /usr/local/bin/projects
docker pokrecem s docker run -it -p 8080:8080 agrdan/gbrobots_image:1 za port forward te na localhost:8080/...
koristim endpointe

- primjetio sam da sam sam zaboravio napraviti endpoint za csv - tako da je to dodano
- dodao sam metodu za provjeru tokena da se ne gomila redundantni kod
"""
u zamjenu za dokumentaciju šaljem postman json sa enpointima koje sam koristio.

Za tipove Robota i Taskova sam koristio nasumično odabrane kodove - Enum klase
RobotType mogu biti 100, 101 i 102
TaskType mogu biti 200, 201 i 202

Drugi dio koji nije riješen je vezan za Docker, na pola je završena priprema image-a, aj jednostavno nisam stigao do kraja.
Aplikacija se vrti na mojem VPSu pa se može direktno koristiti postman import, samo je potrebna "registracija" korisnika

u folderu (postman) 
GideonBrothers->auth->registration: upisati username i password, te je tako izvršena registracija
napraviti login s registriranim podacima iznad da se dobi token, te taj token kopirati u svaki endpoint u header pod property: Auth-Token

controlleri sadrže endpointe (napravio bi endpointe s metodama odvojeno da sam uspio generirati dokumentaciju, s obzirom da nisam uspio generirati dokumentaciju, išao sam na generičko riješenje - redundancija je u dva glavna servisa, tako da bi ako bi razvijao i dalje bi išao svakako na generičko korištenje metode za robot i task service.

datasource - podjeljen na DTO i entitete

changelog - helper util koji mi služi za "one time" generiranje stvari u bazi s tagovima, npr. obično si genereiram test user-a u bazi, enume i slično, te bez potrebe vanjskih XML file-ova (ili sličnih) generiram jednoznačno entitete, te se na temelju tagova provjerava da li je pojedini entitet importan.

servisi - logika koda - spoj između controllera i datasource-a

utils - pomocne klase za jednostavnije riješavanje problema


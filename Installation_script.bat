 @echo uruchamianie kontenera MySQL i Prestashop

@start cmd /k docker-compose up

@echo Wstrzymanie dalszego wykonywania kodu na 90 sekund 

@timeout /t 90

@echo Ladowanie bazy danych MySQL z pliku

@docker exec -i kursy-shop-main_some-mysql_1 mysql -uroot -padmin prestashop < ./db/dbdump.sql

@echo Instalacja certyfikatów 

@docker exec -i kursy-shop-main_some-prestashop_1 a2enmod rewrite
@docker exec -i kursy-shop-main_some-prestashop_1 a2enmod rewrite ssl

@docker cp ./certs/localhost.crt kursy-shop-main_some-prestashop_1:/etc/ssl/certs/ssl-cert-snakeoil.pem
@docker cp ./certs/localhost.key kursy-shop-main_some-prestashop_1:/etc/ssl/private/ssl-cert-snakeoil.key

@docker exec -i kursy-shop-main_some-prestashop_1 a2ensite default-ssl

@docker exec -i kursy-shop-main_some-prestashop_1 service apache2 reload

@echo Sklep prestashop gotowy: https://localhost/
@echo Panel admina Prestashop: https://localhost/admin-daniel/
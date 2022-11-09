Feature: log out

	como usuario
	quiero poder desloguearme
	para validar que figure nuevamente el boton log in

	Scenario:  logout validar el link de log in
		Given el usuario este en la pagina https://www.demoblaze.com/
        And el usuario esta logeado
		When el usuario se deslogea de la pagina
		Then la pagina muestra el link log in
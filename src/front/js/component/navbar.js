import React from "react";
import { Link } from "react-router-dom";
import logotipo from '../../img/logotipo.png';


export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<img src={logotipo} />
				</Link>
				<div className="ml-auto">
					<Link to="/conciertos">
						<button className="btn btn-primary">Conciertos</button>
					</Link>
					<Link to="/musicians">
						<button className="btn btn-primary">Músicos</button>
					</Link>
					<Link to="/bands">
						<button className="btn btn-primary">Bandas</button>
					</Link>
					<Link to="/establishments">
						<button className="btn btn-primary">Locales</button>
					</Link>
					<Link to="/profile/:userId">
						<button className="btn btn-primary">Prueba</button>
					</Link>
				</div>
			</div>
		</nav>
	);
};

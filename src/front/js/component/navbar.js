import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logotipo from "../../img/logotipo.png";

export const Navbar = () => {
	const[img, setImg] = useState()

	useEffect(() => {
		fetch(`${process.env.BACKEND_URL}/api/imagenUser`, {
		  method: "GET",
		  headers: {
			headers: { Authorization: "Bearer " + localStorage.getItem("token") },
			// "Content-Type": "application/json",
		  },
		})
		  .then((response) => {
			return response.json();
		  })
		  .then((result) => {
			setImg(result.img);
			
		  });
	  }, []);
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container">
        <Link to="/">
          <img src={logotipo} />
        </Link>
        <div className="ml-auto">
          <ul class="nav nav-pills">
            <li class="nav-item">
              <a class="nav-link" href="/conciertos">
                conciertos
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/musicians">
                musicians
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/bands">
                bands
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/establishments">
                establishments
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/profile/:userId">
                Perfil
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/login">
                Login
              </a>
            </li>
            <img
              src={img}
              className="rounded-circle"
              style={{ width: "150px" }}
              alt="Avatar"
            />
          </ul>
        </div>
      </div>
    </nav>
  );
};

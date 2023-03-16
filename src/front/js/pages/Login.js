import React, { useEffect, useState } from "react";

export const Login = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  
  const fetchLogin = async() => {
    await fetch(`${process.env.BACKEND_URL}/api/login`, {
      method: "POST",
      header: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    })
      .then((response) => response.json())
      .then((result) => localStorage.setItem("token", result.token));
  } 

  return (
    <>
      <div className="container">
        <div className="row mt-5">
            <div className="col"></div>
            <div className="col-lg-6 border rounded-3 p-5">
                <h1 className="text-center mt-5 mb-5">Login</h1>
        <div className="mb-3 row">
          <label for="inputEmail" className="col-sm-2 col-form-label">
            Email
          </label>
          <div className="col-sm-10">
            <input
              onChange={(e) => setEmail(e.target.value)}
              type="text"
              className="form-control"
              id="inputEmail"
            />
          </div>
        </div>
        <div className="mb-3 row">
          <label for="inputPassword" className="col-sm-2 col-form-label">
            Password
          </label>
          <div className="col-sm-10">
            <input
              onChange={(e) => setPassword(e.target.value)}
              type="password"
              className="form-control"
              id="inputPassword"
            />
          </div>
        </div>
        <button type="button" className="btn btn-warning mt-4 mb-5 FormButton" onClick={fetchLogin}>Enviar</button>
      </div>
      <div className="col"></div>
      </div></div>
    </>
  );
};

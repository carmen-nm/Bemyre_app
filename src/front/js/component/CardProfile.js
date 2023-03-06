import React from "react";
import '../../styles/home.css'




export const CardProfile = ({perfil}) => {
  

  return perfil ? (
    <>
      <div className="card cardProfile">
      <img src={perfil.profile_img} className="card-img-top imagCard" alt="..."/>
      <div className="card-body bodyCard">
        <h5 className="card-title">{perfil.user_instrument.map((element)=>(<span >{element.instrument_name}</span>))} | {perfil.city}</h5>

        <p>{perfil.description}</p>      

      </div>  

    </div>
    </>
  ) : "";
};



import React from "react";
import '../../styles/home.css'




export const CardEstablishment = ({
  establishment_profile_img,
  name,
  city,
  music_genre_establishment,
  description,
  ubicacion
  
  

}) => {
  

  return (
    <>
      <div className="card cardEstablishment">
      <img src={establishment_profile_img} className="card-img-top imagCard" alt="..."/>
      <div className="card-body bodyCard">
        <h5 className="card-title">{name} | {city}</h5>
        <p>{ubicacion}</p>
        <p>{description}</p>       

      </div>  
      <div class="card-footer">
          {music_genre_establishment.map((element)=>(<span className="badge rounded-pill bg-warning m-1">{element.music_genre_name}</span>))}        
      </div>
    </div>
    </>
  );
};



import React from "react";
import '../../styles/home.css'




export const CardConcert = ({
  event_profile_img,
  name,
  description,
  establishment_name,
  music_genre_event,
  ubicacion,
  city,
  date,

}) => {
  

  return (
    <>
      <div className="card cardConcert">
      <img src={event_profile_img} className="card-img-top imagCard" alt="..."/>
      <div className="card-body bodyCard">
        <h5 className="card-title">{name} | {establishment_name}</h5>
        <p className="card-text textosobrante">{description}</p>
        <p className="card-text">{ubicacion} | {city}</p>
        <p className="card-text">{date}</p>
      </div>  
      <div class="card-footer">
          {music_genre_event.map((element)=>(<span className="badge rounded-pill bg-warning m-1">{element.music_genre_name}</span>))}        
      </div>
    </div>
    </>
  );
};



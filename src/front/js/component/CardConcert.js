import React from "react";
import '../../styles/home.css'




export const CardConcert = ({
  event_profile_img,
  name,
  description,
  establishment_name,
  music_genre_event,

}) => {
  

  return (
    <>
      <div className="card cardConcert">
      <img src={event_profile_img} className="card-img-top imagCard" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">{name} | {establishment_name}</h5>
        <p className="card-text">{description}</p>
        {/* <div> */}
          {music_genre_event.map((element)=>(<span className="badge rounded-pill text-bg-secondary">{element.music_genre_id}</span>))}
        {/* </div> */}
      </div>
    </div>
    </>
  );
};

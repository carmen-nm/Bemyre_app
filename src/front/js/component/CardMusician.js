import React from "react";
import '../../styles/home.css'




export const CardMusician = ({
  profile_img,
  artistic_name,
  city,
  music_genre_user,
  user_instrument
  

}) => {
  

  return (
    <>
      <div className="card cardMusician">
      <img src={profile_img} className="card-img-top imagCard" alt="..."/>
      <div className="card-body bodyCard">
        <h5 className="card-title">{artistic_name} | {city}</h5>
        {/* <p>Mi instrumento principal: {user_instrument.map((element)=>(<span className="badge rounded-pill bg-warning m-1">{element}</span>))}</p>        */}
        {/* <p>Mi instrumento principal: {instrument.map((element)=>(<span className="badge rounded-pill bg-warning m-1">{element.instrument_name}</span>))}</p>        */}
        {/* <p>Mi instrumento principal es: {instrument}</p> */}
        <p>Mi instrumento principal: {user_instrument.map((element)=>(<span >{element.instrument_name}</span>))}</p>       

      </div>  
      <div class="card-footer">
          {music_genre_user.map((element)=>(<span className="badge rounded-pill bg-warning m-1">{element.music_genre_name}</span>))}        
      </div>
    </div>
    </>
  );
};



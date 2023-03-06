import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CardBand } from "../component/CardBand";
import { CardProfile } from "../component/CardProfile";
import { CardEstablishment } from "../component/CardEstablishment";


export const ProfileMusician = () => {
  let { userId } = useParams();
  const [perfil, setPerfil] = useState();

  useEffect(() => {
    fetch(`${process.env.BACKEND_URL}/api/profile/${userId}`, {
      method: "GET",
      headers: {
        // Authorization: `Bearer ${getStore().token_local}`,
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        return response.json();
      })
      .then((result) => {
        console.log(result);
        setPerfil(result);
      });
  }, []);
  return (
    <>
      <div className="container  headerProfile ">
       <img className="img-headerProfile" src={perfil?.portrait_img}/>
       <div className="row separacion">
       <div className="col-lg-3"></div>
       <div className="col-lg-9 text-img-headerProfile">
             <h1>{perfil?.artistic_name}</h1>
            <h5>
              {perfil?.first_name} {perfil?.last_name}
            </h5>
       </div>

       </div>
  
        
      </div>
      <div className="container">
        <div className="row">
          <div className="col-lg-3 espaciadocard">
            <CardProfile perfil={perfil} />
          </div>
          <div className="col-lg-9 ">
            
            <div className="row ">
              <h3 className="mt-4 mb-3">Mis música</h3>
              <div className="col-lg-6">
            <iframe className="w-100 h-100" src={`https://open.spotify.com/embed/track/${perfil?.spotify_url}utm_source=generator`}></iframe>

              </div>
              <div className="col-lg-6">
                            <iframe className="w-100 rounded " src={`https://www.youtube.com/embed/${perfil?.youtube_url}`} ></iframe>

              </div>
            </div>
            <div className="row mt-3">
              <h3 className="mt-4 mb-3">Mis instrumentos</h3>
              <p >{perfil?.user_instrument.map((element)=>(<p >{element.instrument_name}</p>))} </p>

              </div>
              <div className="row mt-3">
              <h3 className="mt-4 mb-3">Géneros de música con los que me identifico</h3>
              {perfil?.music_genre_user.map((element)=>(<span className="badge rounded-pill bg-warning m-1 " style={{width: "min-content"}}>{element.music_genre_name}</span>))}

              </div>
              <h3 className="mt-4 mb-3">Mis grupos de música</h3>
              {/* {perfil?.bands.map((element)=>(<span className="badge rounded-pill bg-warning m-1 " style={{width: "min-content"}}>{element.name}</span>))} */}
              {perfil?.bands.map((element)=>(
              <CardBand
              name={element.name}
              description={element.description}
              band_profile_img={element.band_profile_img}
              music_genre_band={element.music_genre_band}
              city = {element.city}
              />
            ))}
              <h3 className="mt-4 mb-3">Mis locales con música en vivo</h3>
              {perfil?.establishments.map((element)=>(
                
                  <CardEstablishment
                    name={element.name}
                    description={element.description}
                    establishment_profile_img={element.establishment_profile_img}
                    music_genre_establishment={element.music_genre_establishment}
                    ubicacion={element.ubicacion}
                    city = {element.city}
                  />
                
              ))}


              </div>
            
          </div>
        </div>
      
    </>
  );
};

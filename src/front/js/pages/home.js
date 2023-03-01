import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Jumbotron } from "../component/Jumbotron";
import { CardConcert } from "../component/CardConcert";
import { CardMusician } from "../component/CardMusician";
import { CardEstablishment } from "../component/CardEstablishment";
import { CardBand } from "../component/CardBand";
import { Footer } from "../component/footer";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container-fluid seccioneshome">
        <h2>Conciertos</h2>

        <div className="rowCards">
          {store.events?.map((element) => (
            <CardConcert
              name={element.name}
              description={element.description}
              event_profile_img={element.event_profile_img}
              establishment_name={element.establishment_name}
              music_genre_event={element.music_genre_event}
              date={element.date}
              hour={element.hour}
              ubicacion={element.ubicacion}
              city = {element.city}
            />
          ))}
        </div>
      </div>
      <div className="container-fluid seccioneshome">
        <h2>Músicos</h2>

        <div className="rowCards">
          {store.musicians?.map((element) => (
            <CardMusician
            profile_img={element.profile_img}
            artistic_name={element.artistic_name}
            city={element.city}
            music_genre_user={element.music_genre_user}
            user_instrument={element.user_instrument}             
            />
            
          ))}
        </div>
      </div>
      <div className="container-fluid seccioneshome">
        <h2>Locales</h2>

        <div className="rowCards">
          {store.establishments?.map((element) => (
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
      <div className="container-fluid seccioneshome">
        <h2>Bandas de música</h2>

        <div className="rowCards">
          {store.bands?.map((element) => (
            <CardBand
              name={element.name}
              description={element.description}
              band_profile_img={element.band_profile_img}
              music_genre_band={element.music_genre_band}
              city = {element.city}
            />
          ))}
        </div>
      </div>
      <Footer/>
    </>
  );
};

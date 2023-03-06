import React, { useContext } from "react";
import { CardBand } from "../component/CardBand";
import { Jumbotron } from "../component/Jumbotron";
import { Context } from "../store/appContext";

export const Bands = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container ">
        <h2 className="text-center mt-5 mb-5">Bandas de música cerca de ti</h2>
        
          <div className=" d-flex flex-wrap justify-items-center gap-2">
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
    </>
  );
};

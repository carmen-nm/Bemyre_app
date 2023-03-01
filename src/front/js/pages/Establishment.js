import React, { useContext } from "react";
import { CardEstablishment } from "../component/CardEstablishment";
import { Jumbotron } from "../component/Jumbotron";
import { Context } from "../store/appContext";

export const Establishment = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container ">
        <h2 className="text-center mt-5 mb-5">Locales con música en vivo</h2>
        
          <div className=" d-flex flex-wrap justify-items-center ">
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
    </>
  );
};

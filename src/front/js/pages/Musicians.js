import React, { useContext } from "react";
import { CardMusician } from "../component/CardMusician";
import { Jumbotron } from "../component/Jumbotron";
import { Context } from "../store/appContext";

export const Musicians = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container ">
        <h2 className="text-center mt-5 mb-5">Músicos cerca de ti</h2>
        
          <div className=" d-flex flex-wrap justify-items-center gap-2">
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
    </>
  );
};

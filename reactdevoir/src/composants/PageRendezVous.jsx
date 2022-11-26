import React, { useEffect } from "react";

import { useNavigate } from "react-router-dom";
import { useSearchParams } from 'react-router-dom';

function PageRendezVous() {
  let navigate = useNavigate();

  useEffect(() => {
    navigate("/");
  }, []);

  return (
    <form >
      <div>
        <label for="title">Title : </label>
        <input type="text" name="title" id="title" required />
      </div>
      <div>
        <label for="comment">Commentaires : </label>
        <input type="text" name="comment" id="comment" required />
      </div>
      <div>
        <label for="date">Date : </label>
        <input type="date" name="date" id="date" required />
      </div>
      <div>
        <input type="submit" value="Prendre rendez-vous" />
      </div>
    </form>
  );
}

export default PageRendezVous;

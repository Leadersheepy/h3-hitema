//Une partie en tête dans laquelle on affiche le mois et l'année en cours et 
//des boutons permettant de passer au mois précédent / mois suivant et/ou à 
//l'année précédente / année suivante.

function EnTeteCalendrier(props) {
    const lesMois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"];

    return(
        <div className="container">
             <button className="jolieBouton" onClick={() => {props.changementDeMois(-1)}}>{"<<"}</button> {lesMois[props.mois]} <button className="jolieBouton" onClick={() => props.changementDeMois(1)}>{">>"}</button> <br />
             <button className="jolieBouton" onClick={() => {props.changementAnnee(-1)}}>{"<<"}</button> {props.annee} <button className="jolieBouton" onClick={() => {props.changementAnnee(1)}}>{">>"}</button> <br />
      
         </div>
    );
}

export default EnTeteCalendrier;
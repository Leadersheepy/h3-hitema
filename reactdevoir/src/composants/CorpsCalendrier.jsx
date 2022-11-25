const CorpsCalendrier = (props) => {

function jourParMois(annee, mois) {
    return new Date(annee, mois + 1, 0).getDate();
}

let d = new Date();
let taille = jourParMois(props.annee, props.mois);
let tailleDuPrecedentMois = jourParMois(props.annee, props.mois - 1);
let premierJour = (new Date(props.annee, props.mois)).getDay();

    let jours = [];
    let index = 1;

    for (let i = 0; i < 6; i++) {
        let semaine = [];
        for (let j = 0; j < 7; j++) {
            if (i ==0 && j < premierJour - 1) {
                semaine.push({
                    'type': 'mois-precedent',
                    'value': tailleDuPrecedentMois - (premierJour - 1 - j)
                });
            } else if (index > taille) {
                semaine.push({
                    'type': 'prochain-mois',
                    'value': index - taille
                });
                index++;
            } else {
                semaine.push({
                    'type': 'mois',
                    'value': index
                });
                index++;
            }
        }
        jours.push(semaine);
    }


    return (
    <div>
        <table>
            <thead className="container">
                <tr className="row">
                    <th className="col jour">LU</th>
                    <th className="col jour">MA</th>
                    <th className="col jour">ME</th>
                    <th className="col jour">JE</th>
                    <th className="col jour">VE</th>
                    <th className="col jour">SA</th>
                    <th className="col jour">DI</th>  
                </tr>
            </thead>
            <tbody>
                {jours.map((val) => {

                    return (
                    <div className="row">
                        <div className="col">
                    {val.map((val) => {return (  
                    <label className={(d.getDate() == val.value && d.getMonth() == props.mois && d.getFullYear() == props.annee) ? 'aujourdhui '  : 'jour ' + val.type}>
                    <label className="effet-de-passage" href={"/meet_list?date=" + val.value + "-" + props.mois + "-" + props.annee}>{val.value}</label>
                    
                    </label>)})}
                    </div>
                    </div>)
                        
                        })}
            </tbody> 

        </table>
    </div>
    );
}
 
export default CorpsCalendrier; 
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { getAllDesigns, clearData } from "../../store/designs";

export default function UserDesigns() {
  const designs = useSelector(state => state.designs.allDesigns);
  const desArr = Object.values(designs);
  const dispatch = useDispatch();
  const history = useHistory();
  console.log('DESARR', desArr)

  useEffect(() => {
    dispatch(getAllDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div className="recent-des">
      {desArr.map(des => (
        <div className="des-containers" onClick={() => history.push(`/designs/${des.id}/${des.template[0].alias}`)}>
          <h3>{des.name}</h3>
        </div>
      ))}
    </div>
  )
}

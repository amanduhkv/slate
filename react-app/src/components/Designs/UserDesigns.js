import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllUserDesigns, clearData } from "../../store/designs";

export default function UserDesigns() {
  const designs = useSelector(state => state.designs.allDesigns);
  const desArr = Object.values(designs);
  const dispatch = useDispatch();
  console.log('DESARR', desArr)

  useEffect(() => {
    dispatch(getAllUserDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      {desArr.map(des => (
        <div className="des-containers">
          {des.name}
        </div>
      ))}
    </div>
  )
}

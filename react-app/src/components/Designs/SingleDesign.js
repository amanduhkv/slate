import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getADesign, clearData } from "../../store/designs";

export default function SingleDesign() {
  const { designId } = useParams();
  const user = useSelector(state => state.session.user);
  const singleDesign = useSelector(state => state.designs.singleDesign)
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getADesign(designId))

    return () => dispatch(clearData())
  }, [dispatch, designId])

  if (!singleDesign) return null;

  return (
    <div>
      Single Design Page
    </div>
  )
}

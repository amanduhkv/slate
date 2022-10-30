import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { getAllUserDesigns, clearData } from "../../store/designs";

export default function UserDesigns() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllUserDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      User's Designs page
    </div>
  )
}

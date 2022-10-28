import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllDesigns, clearData } from "../../store/designs";

export default function Designs() {
  // const designs = useSelector(state => state.designs.allDesigns)
  // console.log('THE DESIGNS', designs)

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllDesigns())

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      Designs page
    </div>
  )
}

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getAllUserBrands, clearData } from "../../store/brands";

export default function UserBrands() {
  const brands = useSelector(state => state.brands.allBrands);
  const brandArr = Object.values(brands);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllUserBrands());

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      <h1>Brand</h1>
      User's Brands Here
    </div>
  )
}

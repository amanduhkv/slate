import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getABrand, clearData } from "../../store/brands";

export default function SingleBrand() {
  const { brandId } = useParams();
  // const brands = useSelector(state => state.brands.allBrands);
  // const brandArr = Object.values(brands);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getABrand(brandId));

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      Single Brand Here
    </div>
  )
}

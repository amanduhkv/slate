import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllBrands, clearData } from "../../store/brands";

export default function Brands() {
  const brands = useSelector(state => state.brands.allBrands);
  const brandArr = Object.values(brands);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllBrands());

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      <h1>Brand</h1>
      <button> + Add new</button>
      <div>Name of Brand Kit Here</div>
      <div>
        <h2>Brand logos</h2>
        <div>box for logos</div>
      </div>
      <div>
        <h2>Brand colors</h2>
        <div>box for colors</div>
      </div>
      <div>
        <h2>Brand fonts</h2>
        <div>box for fonts</div>
      </div>
    </div>
  )
}

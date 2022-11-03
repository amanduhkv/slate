import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { deleteBrand } from "../../store/brands";

export default function DeleteBrand() {
  const brand = useSelector(state => state.brands.singleBrand);
  const dispatch = useDispatch();
  const history = useHistory();

  const handleDelete = async e => {
    e.preventDefault();

    const deletion = await dispatch(deleteBrand(brand.id));
    if (deletion) history.push('/brand');
  };

  return (
    <button id='create-des-button' onClick={handleDelete}>Remove brand</button>
  )
};

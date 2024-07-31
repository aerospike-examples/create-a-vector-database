// import { useEffect, useRef, useState } from 'react';
import { useEffect, useState } from 'react';
import styles from './index.module.css';

const Browser = () => {
	const [products, setProducts] = useState([])
	const [selectedProduct, setSelectedProduct] = useState("");
	const [selectedProductName, setSelectedProductName] = useState("");
	const [dataLoading, setDataLoading] = useState(false)

	const fetchData = async (extraProducts) => {
		let url = extraProducts ? "http://localhost:8085/rest/v1/get_extra_products/"
								: "http://localhost:8085/rest/v1/get_products/"
		fetch(url, {
			method: "GET",
		})
		.then((response) => {
			return response.json()
		})
		.then((data) => {
			console.log(data);
			setProducts(data);
			setSelectedProduct("")
			setSelectedProductName("")
		});
	}

	useEffect(() => {
		fetchData(false);
	}, [])

	const productChange = (e) => {
		let newProductType = e.target.value
		setSelectedProduct(newProductType);
		let products = filterByProductAndSort(newProductType);
		if (products.length > 0) {
			setSelectedProductName(products[0].name);
		}
	}

	const productNameChange = (e) => {
		setSelectedProductName(e.target.value);
	}

	const filterByProductAndSort = (newProductType) => {
		const results = products.filter(p => p.type === newProductType);
		return results.sort()
	}

	const getSelectedProduct = () => {
		const results = products.filter(p => p.type === selectedProduct && p.name === selectedProductName);
		if (results.length > 0) {
			return results[0];
		}
		return null;
	}

	const loadProducts = () => {
		console.log("Loading extra products");
		setDataLoading(true);
		fetchData(true)
		.catch((err) => window.alert("Error loading products: " + err))
		.finally(() => setDataLoading(false));
	}

	return (
		<div className={styles.content}>
			<div className={styles.container}>
				<label htmlFor="productDropdown">Select an option:</label>
				<select id="productDropdown" name="productDropdown" defaultValue={""} onChange={productChange}>
					<option value="" disabled>Select a product type</option>
					<option value="Checking Product">Checking Product</option>
					<option value="Credit Card Product">Credit Card Product</option>
					<option value="Line of Credit">Line of Credit</option>
					<option value="Mortgage Product">Mortgage Product</option>
					<option value="Mutual Funds">Mutual Funds</option>
					<option value="Savings Product">Savings Product</option>
					<option value="Wealth Management">Wealth Management</option>
				</select>
				
				<label htmlFor="productName">Product name:</label>
				<select id="productName" name="productName" onChange={productNameChange}>
					{filterByProductAndSort(selectedProduct).map((product) => {
						return (
							<option key={product.name} value={product.name}>{product.name}</option>
						)
					})}
				</select>

				<label htmlFor="productDesc">Product Description:</label>
				<div id="productDesc" name="productDesc" className={styles.productDesc}>
					{getSelectedProduct() && getSelectedProduct().feature}
				</div> 

				<span>Total products: {products.length}</span>
				<div className={styles.buttonContainer}>
					<button className={styles.button} disabled={dataLoading} onClick={loadProducts}>
						{dataLoading ? 'Loading...' : 'Load Products From CSV'}</button>
				</div>
			</div>
		</div>
	)
}

export default Browser;

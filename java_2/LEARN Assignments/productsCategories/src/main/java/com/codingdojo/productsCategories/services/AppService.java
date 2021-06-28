package com.codingdojo.productsCategories.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.productsCategories.models.Category;
import com.codingdojo.productsCategories.models.Product;
import com.codingdojo.productsCategories.repositories.CategoryRepository;
import com.codingdojo.productsCategories.repositories.ProductRepository;

@Service
public class AppService {

	private final ProductRepository prodRepo;
	private final CategoryRepository catRepo;
	
	public AppService(ProductRepository prodRepo, CategoryRepository catRepo) {
		this.prodRepo = prodRepo;
		this.catRepo = catRepo;
	}
	
//	find ALL
	
	public List<Product> findAllProducts() {
		return (List<Product>) this.prodRepo.findAll();
	}
	
//	CREATE
	
	public Product createProduct(Product p) {
		return this.prodRepo.save(p);
	}
	
	public Product getOneProduct(Long id) {
		return this.prodRepo.findById(id).orElse(null);
	}
	
//	Get CATEGORIES
	
	public List<Category> findAllCategories() {
		return (List<Category>) this.catRepo.findAll();
	}
	
//	Add products to categories. MANY TO MANY.
	
	public void joinProductsToCategories(Long productId, Long categoryId) {
		Product p = this.prodRepo.findById(productId).orElse(null);
		Category c = this.catRepo.findById(categoryId).orElse(null);
		
		c.getProducts().add(p);
		this.prodRepo.save(p);
	}
}

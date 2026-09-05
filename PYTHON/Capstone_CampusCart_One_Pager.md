# Capstone One-Pager — CampusCart

**MVP checklist** for CampusCart (learners).

## Title

**CampusCart** — College E-Commerce & Booking Portal

CampusCart is the college storefront; it uses the same catalog / cart / order patterns as **Swiggy**. Batch alts: MediBook Clinic → **Apollo Hospitals**, teller portal → **HDFC Bank**.

## Stack

Django 5.x · MySQL · HTML/CSS/JS · GitHub · (stretch) DRF + React

## MVP features

1. Register / login / logout  
2. Catalog list + detail + search  
3. Cart + place order  
4. Order history  
5. Admin catalog & order management  
6. Responsive UI + validation  
7. Deployed demo + README  

## Schema (text ER)

```
Category 1──* Product
User 1──* Order 1──* OrderItem *──1 Product
```

## UI pages

Home · Product detail · Cart/Checkout · Orders · Login/Register · Admin/Staff

## GitHub milestones

M0 Repo → M1 Auth shell → M2 Models/Admin → M3 Orders → M4 Deploy → M5 API/React (opt) → M6 Defense

## Defense (10 min)

Problem → Demo → Schema → Hardest bug → Next feature

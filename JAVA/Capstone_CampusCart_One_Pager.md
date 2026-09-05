# Capstone One-Pager — CampusCart (Java)

**MVP checklist** for CampusCart (learners).

## Title

**CampusCart** — College E-Commerce & Booking Portal

CampusCart is the college storefront; it uses the same catalog / cart / order patterns as **Swiggy**. Batch alts: MediBook Clinic → **Apollo Hospitals**, teller portal → **HDFC Bank**.

## Stack

Spring Boot 3.x · MySQL · REST (JSON) · HTML/CSS/JS · GitHub · (stretch) React storefront · (optional) Thymeleaf overview pages

## MVP features

1. Register / login / logout (JWT lite or session — junior-realistic)  
2. Catalog list + detail + search  
3. Cart + place order  
4. Order history  
5. Admin catalog & order management  
6. Validation on write APIs (and UI where present)  
7. Deployed demo + README  

## Schema (text ER)

```
Category 1──* Product
User 1──* Order 1──* OrderItem *──1 Product
```

## UI / API surfaces

REST (must): products, cart, orders, auth  
Pages: Home · Product detail · Cart/Checkout · Orders · Login/Register · Admin/Staff  
Stretch: React listing consuming the same API · short Thymeleaf catalog

## GitHub milestones

M0 Repo + Maven + README → M1 Auth shell → M2 JPA catalog → M3 Orders → M4 Deploy → M5 React (opt) → M6 Defense

## Defense (10 min)

Problem → Demo → Schema → Hardest bug → Next feature

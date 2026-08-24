# Tested Toolchain Guide

Pin these versions for the batch. Update this file when you re-test.

**Last verified profile:** Java Full Stack batch kit (macOS + Windows learners)

## Required versions

| Tool | Version target | Check command |
|------|----------------|---------------|
| JDK | **17 LTS** (prefer for India hiring; **21 LTS** also fine) | `java -version` · `javac -version` |
| Maven | **3.9+** | `mvn -version` |
| Git | 2.40+ | `git --version` |
| MySQL Server | **8.0+** | `mysql --version` |
| Node.js | **20 LTS** (or 22 LTS) — React weeks | `node --version` |
| npm | comes with Node | `npm --version` |
| Spring Boot | **3.x** (Jakarta; `jakarta.*` not `javax.*`) | `pom.xml` parent |
| Vite / React | Vite 5/6 + React 18+ | `npm create vite@latest` |
| Postman | latest stable | Help → About |
| VS Code **or** IntelliJ IDEA Community | latest stable | Help → About |

Prefer **JDK 17** as the class default. Mention 21 so learners are not surprised on JDs. Do not mix 8 / 11 as the teaching JDK.

## Maven / Spring (typical project)

```xml
<!-- Spring Boot 3.x parent; Java 17 -->
<!-- Starters you will actually teach: -->
spring-boot-starter-web
spring-boot-starter-data-jpa
spring-boot-starter-validation
spring-boot-starter-security
spring-boot-starter-test          <!-- JUnit 5 -->
mysql-connector-j
```

Optional stretch (never required in Done when): Lombok, Thymeleaf full CRUD, Spring AI / HTTP call to an LLM API.

React app: create with Vite; add `axios` only if the batch prefers it over `fetch`.

**Config:** `application.yml` + `.env.example`. Never commit secrets.

## IDE extensions / plugins

**VS Code**

- Extension Pack for Java (Microsoft)
- Maven for Java
- Spring Boot Extension Pack (optional)
- ESLint / Prettier (React weeks)
- GitLens (optional)

**IntelliJ Community**

- Bundled Maven + Git
- Do **not** require Ultimate for this course (no paid Spring diagrams)

MySQL Workbench is the default GUI. Postman for REST.

## Install cheat sheet

### macOS (Homebrew)

```bash
brew install openjdk@17 maven git mysql node@20
# Put JDK 17 on PATH (Homebrew prints the exact export)
brew services start mysql
```

### Windows

1. Eclipse Temurin 17 MSI (or Oracle JDK 17) — tick **Add to PATH**  
2. Maven ZIP or `winget install Apache.Maven`  
3. Git for Windows  
4. MySQL Installer (Server + Workbench)  
5. Node LTS MSI  
6. Optional: IntelliJ Community installer  

Confirm:

```bash
java -version
javac -version
mvn -version
git --version
mysql --version
```

## Known fixes

| Symptom | Fix |
|---------|-----|
| `java` / `javac` not found | JDK 17 installer PATH; new terminal |
| `JAVA_HOME` points at 8 or JRE | Set `JAVA_HOME` to the JDK 17 folder |
| `mvn` not found | Maven `bin` on PATH |
| Port 8080 in use | `server.port: 8081` in `application.yml` |
| `javax.*` compile errors on Boot 3 | Use `jakarta.*` |
| Vite CORS to Spring | `@CrossOrigin` (dev) or `CorsConfiguration` — production origins in config |
| MySQL Public Key Retrieval | Document in JDBC/JPA module (do not paste passwords into git) |
| IntelliJ “SDK not selected” | File → Project Structure → SDK 17 |

## Day-0 checklist

- [ ] Paste version outputs (`java`, `javac`, `mvn`, `git`, `mysql`, `node`) in the shared sheet  
- [ ] One sample Spring Boot + MySQL project starts on your laptop (`mvn spring-boot:run`)  
- [ ] One Vite app starts with `npm run dev`  
- [ ] GitHub account + SSH/HTTPS push works  
- [ ] Postman installed  

Lab assets assume this toolchain: [`15_Lab_Assets/`](15_Lab_Assets/).

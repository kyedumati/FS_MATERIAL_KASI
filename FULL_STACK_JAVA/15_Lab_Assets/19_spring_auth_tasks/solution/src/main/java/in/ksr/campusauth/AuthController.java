package in.ksr.campusauth;

import java.util.Map;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final AppUserRepository users;
    private final PasswordEncoder encoder;
    private final JwtService jwtService;

    public AuthController(
            AppUserRepository users, PasswordEncoder encoder, JwtService jwtService) {
        this.users = users;
        this.encoder = encoder;
        this.jwtService = jwtService;
    }

    @PostMapping("/register")
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<?> register(@Valid @RequestBody RegisterRequest incoming) {
        String email = incoming.getEmail().trim().toLowerCase();
        if (users.existsByEmail(email)) {
            return ResponseEntity.status(HttpStatus.CONFLICT)
                    .body(Map.of("error", "Email already registered"));
        }
        AppUser user = new AppUser();
        user.setEmail(email);
        user.setPasswordHash(encoder.encode(incoming.getPassword()));
        users.save(user);
        String token = jwtService.createToken(email);
        return ResponseEntity.status(HttpStatus.CREATED).body(new AuthResponse(token, email));
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@Valid @RequestBody LoginRequest incoming) {
        String email = incoming.getEmail().trim().toLowerCase();
        AppUser user = users.findByEmail(email).orElse(null);
        if (user == null || !encoder.matches(incoming.getPassword(), user.getPasswordHash())) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                    .body(Map.of("error", "Bad email or password"));
        }
        return ResponseEntity.ok(new AuthResponse(jwtService.createToken(email), email));
    }
}

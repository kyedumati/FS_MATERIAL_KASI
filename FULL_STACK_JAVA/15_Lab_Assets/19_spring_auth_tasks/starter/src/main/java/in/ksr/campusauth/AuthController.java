package in.ksr.campusauth;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    // TODO: inject AppUserRepository, PasswordEncoder, JwtService

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest incoming) {
        // TODO: @Valid; lowercase email; 409 if exists; encode password; 201 + AuthResponse
        return ResponseEntity.ok().build();
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest incoming) {
        // TODO: @Valid; 401 if missing user or password mismatch (same message either way)
        return ResponseEntity.ok().build();
    }
}

package in.ksr.campusauth;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final AppUserRepository users;

    public AuthController(AppUserRepository users) {
        this.users = users;
    }

    @PostMapping("/register")
    @ResponseStatus(HttpStatus.CREATED)
    public AuthResponse register(@RequestBody RegisterRequest incoming) {
        AppUser user = new AppUser();
        user.setEmail(incoming.getEmail());
        // BROKEN: stores the raw password. Hash with PasswordEncoder.encode
        user.setPasswordHash(incoming.getPassword());
        users.save(user);
        return new AuthResponse("not-a-jwt", incoming.getEmail());
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest incoming) {
        AppUser user = users.findByEmail(incoming.getEmail()).orElse(null);
        if (user == null || !incoming.getPassword().equals(user.getPasswordHash())) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
        }
        return ResponseEntity.ok(new AuthResponse("not-a-jwt", incoming.getEmail()));
    }
}

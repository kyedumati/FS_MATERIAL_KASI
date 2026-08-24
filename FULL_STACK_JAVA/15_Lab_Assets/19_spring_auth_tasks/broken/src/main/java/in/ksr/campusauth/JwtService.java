package in.ksr.campusauth;

import org.springframework.stereotype.Component;

@Component
public class JwtService {

    // BROKEN: not a signed JWT. Use jjwt builder + env secret.
    public String createToken(String email) {
        return "fake." + email + ".token";
    }

    public String parseEmail(String token) {
        return "nobody@example.com";
    }
}

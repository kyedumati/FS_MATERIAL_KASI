package in.ksr.campusauth;

import org.springframework.stereotype.Component;

@Component
public class JwtService {

    // TODO: read app.jwt.secret and app.jwt.expiry-minutes from yml
    // TODO: createToken(email) and parseEmail(token) with jjwt 0.12 (signWith / verifyWith)

    public String createToken(String email) {
        return email;
    }

    public String parseEmail(String token) {
        return token;
    }
}

package in.ksr.campusauth;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {

    // TODO: inject JwtAuthFilter
    // TODO: csrf disable, STATELESS session
    // TODO: permit /auth/** and GET /products; any other request authenticated
    // TODO: addFilterBefore jwt filter, UsernamePasswordAuthenticationFilter
    // TODO: lite 401 JSON {"error":"Unauthorized"}

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable());
        return http.build();
    }
}

package in.ksr.campusauth;

import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class AppUserDetailsService implements UserDetailsService {

    private final AppUserRepository users;

    public AppUserDetailsService(AppUserRepository users) {
        this.users = users;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        AppUser found = users.findByEmail(username).orElse(null);
        if (found == null) {
            throw new UsernameNotFoundException(username);
        }
        return User.withUsername(found.getEmail())
                .password(found.getPasswordHash())
                .roles("USER")
                .build();
    }
}

package in.ksr.campusauth;

import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AppUserRepository extends JpaRepository<AppUser, Long> {

    // TODO: findByEmail, existsByEmail
    Optional<AppUser> findByEmail(String email);

    boolean existsByEmail(String email);
}

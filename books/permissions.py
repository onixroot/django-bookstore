def allow_special_status(private_file):
    request = private_file.request
    return request.user.is_authenticated and request.user.has_perm('books.special_status')
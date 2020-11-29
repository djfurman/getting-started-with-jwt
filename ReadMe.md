# JWT Examples

As we look toward better end-to-end verifications, distributed systems can introduce new challenges. One of these is how to verify that a message from a system actually came from that authorized systems.

Numerous authorizers are available and layer-4 security can give you some measure of assurance, but stateful and stateless firewall maintenance is only the first step, not to mention that likely your service has more than one customer!

Given the need for this support; a best practices guide has been developed and maintained by IEFT. You can find it as [RFC-8725](https://www.rfc-editor.org/rfc/rfc8725.html)

## JWT is not complex

While many crypto-security measures can be difficult to implement, this repo is provided as a simple example of what it takes to generate and work with JWT keys, and even automatically build rotatable keys via code.

As you look through the examples, you can see that these tokens can be generated and verified in less than 50 lines of code.

### Reference implementations

As a note, while the examples all work as reference implementations. When implementing, bear in mind that secure keys need to be stored in an operations environment (i.e., symmetric secrets, asymmetric private keys) inside of an authenticated and secure storage mechanism.

### Getting help

If you are not familiar with the types of services needed please find an expert, or reach out to me on Twitter [@djfurman4tech](https://twitter.com/djfurman4tech) and I'll be happy to send you some resources for your use case.

## Diving In

### Navigating the Demo

There are three key demo components.

1. [`shared_secret_example.py`](./shared_secret_example.py)
1. [`key_rotation.py`](./key_rotation.py)
1. [`asymmetric_key_example.py`](./asymmetric_key_example.py)

The shared secret example is a demonstration of simple symmetric (shared key) implementation; to use this you'll need to setup the shared key following the instructions below.

For the asymmetric examples (public/private key infrastructure), I've included a generation script that can also be a reference for generating rotating encryption key IDs for a JWK or JWS solution. Run that first, then edit the file to point to the appropriate key. If you're comfortable with OpenSSL, feel free to avoid the automation here. It's just provided for convenience and reference.

### Running the Demo

1. Clone this repository
1. Run `pipenv sync` to install hashed dependencies
1. Run `cp .env.example .env`
1. Run `openssl rand -base64 64` and copy the result to `.env`'s KEY property
1. Run `pipenv shell` to access the virtual environment and load your `.env` file
1. Review the file, then run `python shared_secret_example.py`
1. Run `python key_rotation.py` to generate a new asymmetric RSA keys
1. Edit the `asymmetric_key_example.py` file to map to your generated public and private key names respectively
1. Review the file, then run `python asymmetric_key_example.py`
1. Notice that the `asymmetric_key_example.py` file includes additional claim validation parameters based on a fake service demo
1. I've intentionally included a `time.sleep(3)` line in the asymmetric example. Comment out the line for the `leeway` keyword argument and watch the system catch the expiration error!

## Next Steps

### Expanding the Demo

I'm using a simple RSA key-pair here, there is no reason we couldn't add Elliptic Curve support, and if there is interest I'm happy to demonstrate and add it.

### The JWT Solution(s)

Json Web Tokens (JWTs) described in [RFC-7519 Section 3](https://tools.ietf.org/html/rfc7519#section-3) provide a method to set the claims of an API call via an encrypted header using symmetric or asymmetric keys.

These then can be used to run validation of the payload of the message; or send an unauthenticated header with a key ID, then fetch the key and use a rotating key cryptography verify the source of the message.

RFCs implementing these security handoffs using JWT include:

- JSON Web Key (JWK) [RFC-7517 Section 3](https://tools.ietf.org/html/rfc7517#section-3)
- JSON Web Signature (JWS) [RFC-7515 Section 4](https://tools.ietf.org/html/rfc7515#section-4)

### Contribution/Errata

If you'd like to see something else added to this demonstration, or you find an error, please open an issue or a pull request. I always welcome collaboration.

If you find a security issue, please drop a message detailing the issue in [my HawkPost box](https://hawkpost.co/box/61585f44-cfa4-4b50-9b76-65c51db64f48) which will send me an encrypted note. You can also reach out to me using [my gpg public key](https://gist.github.com/djfurman/b8d841fa873c3a0ae800580a2a62e529), if you are familiar with gpg.

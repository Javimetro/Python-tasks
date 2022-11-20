from flask import Flask, request

app = Flask(__name__)


@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = int(args.get('luku'))
    print(luku)
    if luku == 1:
        vastaus = {
            'luku': luku,
            'alkuluku': False,

        }
    elif luku == 2:
        vastaus = {
            'luku': luku,
            'alkuluku': True,

        }
    else:
        for i in range(2, luku):
            if luku % i == 0:
                vastaus = {
                    'luku': luku,
                    'alkuluku': False

                }
                break
        else:
            vastaus = {
                'luku': luku,
                'alkuluku': True

            }
    test_vastaus = str(vastaus)

    return test_vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

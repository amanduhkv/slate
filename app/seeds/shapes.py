from app.models import db, Shape

shapes = [
  {
    'id': 1,
    'name': 'arch-down',
    'url': 'https://drive.google.com/uc?export=view&id=1OTMK8uGACMxHIwC_Rv7IHaQdNvv-RuFT'
  },
  {
    'id': 2,
    'name': 'arch-up',
    'url': 'https://drive.google.com/uc?export=view&id=19MdxIrt27kbnCCjM5uQA09eVWV8d2Yk3'
  },
  {
    'id': 3,
    'name': 'cloud',
    'url': 'https://drive.google.com/uc?export=view&id=1vgf9BkWgtwyEgFfuT13J3Kr2Y2xvqdIs'
  },
  {
    'id': 4,
    'name': 'double-arrow',
    'url': 'https://drive.google.com/uc?export=view&id=10qoAwYeoT063DlQyC-y-JfdQ2q9_HXTP'
  },
  {
    'id': 5,
    'name': 'down-arrow',
    'url': 'https://drive.google.com/uc?export=view&id=1K-U6mYNwb7Mg5-maJbEEltjQVm5PXANN'
  },
  {
    'id': 6,
    'name': 'filled-circle',
    'url': 'https://drive.google.com/uc?export=view&id=1EhIdge7jwlKkDtsAztr4O-G291DRLDZg'
  },
  {
    'id': 7,
    'name': 'filled-diamond',
    'url': 'https://drive.google.com/uc?export=view&id=11jQZAUs4qKJ71y1xIfE3naiJNTjT8r4i'
  },
  {
    'id': 8,
    'name': 'filled-hexagon',
    'url': 'https://drive.google.com/uc?export=view&id=11x8Oz71Vz71JFaX8QLS-S48sEP96f3B2'
  },
  {
    'id': 9,
    'name': 'filled-octagon',
    'url': 'https://drive.google.com/uc?export=view&id=1diT1zuYYsVV2yHPK6eUhruXV_cebv40E'
  },
  {
    'id': 10,
    'name': 'filled-pentagon',
    'url': 'https://drive.google.com/uc?export=view&id=1DSOzssVgk79fBeLS9osnv6Ac-tX0k1IA'
  },
  {
    'id': 11,
    'name': 'filled-square',
    'url': 'https://drive.google.com/uc?export=view&id=1lsJYVPChG6_rugo5xNjAUby9-noL49YV'
  },
  {
    'id': 12,
    'name': 'filled-star',
    'url': 'https://drive.google.com/uc?export=view&id=1zcpn_Ixeaw0CRnGAUaiFtKOaGuWG4NDK'
  },
  {
    'id': 13,
    'name': 'filled-triangle',
    'url': 'https://drive.google.com/uc?export=view&id=1yb3gwoNi9S4mvDVIuHKdEG1LMnWxSfxi'
  },
  {
    'id': 14,
    'name': 'heart',
    'url': 'https://drive.google.com/uc?export=view&id=1gxpwIBqPHlX0VaafIdjkpo-Jk4l9HyGb'
  },
  {
    'id': 15,
    'name': 'left-arrow',
    'url': 'https://drive.google.com/uc?export=view&id=1D_seG3FJufnrqoI-zM5jIUJ0Ii-b2N6b'
  },
  {
    'id': 16,
    'name': 'plus',
    'url': 'https://drive.google.com/uc?export=view&id=1f2dto1oRmf_ARb6yA7iMVKvz5bxAKawy'
  },
  {
    'id': 17,
    'name': 'right-arrow',
    'url': 'https://drive.google.com/uc?export=view&id=1A3xzuO6wnnwW43yvDTbe58yzkyc7UdFC'
  },
  {
    'id': 18,
    'name': 'speech-round',
    'url': 'https://drive.google.com/uc?export=view&id=1VeLPfOz4FLrCDqWcYEuHT4_lBhpEUwhE'
  },
  {
    'id': 19,
    'name': 'speech-square',
    'url': 'https://drive.google.com/uc?export=view&id=1F1-EQm7FUA4hbo-_4mXFlAmXhR6mGH1R'
  },
  {
    'id': 20,
    'name': 'up-arrow',
    'url': 'https://drive.google.com/uc?export=view&id=1wxXq3vxjj2QGoueW8klEmzxjVgaH9_d5'
  },
]


instances = []


for shape in shapes:
    instances.append(Shape(
      name = shape['name']
      url = shape['url']
    ))


def seed_shapes():
  for i in instances:
    db.session.add(i)
  db.session.commit()


def undo_seed_shapes():
  db.session.execute('TRUNCATE shapes RESTART IDENTITY CASCADE;')
  db.session.commit()

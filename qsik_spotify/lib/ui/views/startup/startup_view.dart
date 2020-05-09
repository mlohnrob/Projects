import 'package:flutter/material.dart';
import 'package:stacked/stacked.dart';

import 'package:qsik_spotify/ui/views/startup/startup_view_model.dart';

class StartUpView extends StatelessWidget {
  const StartUpView({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ViewModelBuilder<StartUpViewModel>.nonReactive(
      viewModelBuilder: () => StartUpViewModel(),
      onModelReady: (model) => model.handleStartUpLogic(),
      builder: (context, model, child) => Scaffold(
        backgroundColor: Colors.white,
        body: Center(
          child: Text("Hello World!"),
        ),
      ),
    );
  }
}
